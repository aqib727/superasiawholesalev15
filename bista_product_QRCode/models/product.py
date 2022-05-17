import qrcode
import base64
from io import BytesIO
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    qr_code = fields.Binary("QR Code", attachment=True, store=True)
    qr_data_url = fields.Char("QR Code Data/URL", store=True, tracking=1)

    @api.onchange('qr_data_url')
    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.qr_data_url)
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        self.qr_code = qr_image

    @api.model
    def create(self, values):
        res = super(ProductTemplate, self).create(values)
        action_id = self.env.ref('stock.product_template_action_product')
        base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        base_url += '/web#id=%d&action=%d&view_type=form&model=product.template' % (
            res.id, action_id.id)
        if base_url:
            res.with_context(not_to_repeat=True).qr_data_url = base_url
            res.generate_qr_code()
        return res

    @api.model
    def write(self, values):
        res = super(ProductTemplate, self).write(values)
        for record in self:
            if not self._context.get('not_to_repeat') and values.get('qr_data_url'):
                record.generate_qr_code()
        return res
