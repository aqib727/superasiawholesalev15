from odoo import fields, models

# FIXME: Need to move below code to superasiab2b_b2c module
class SaleOrder(models.Model):
    _inherit = "sale.order"

    b2b_confirmed = fields.Boolean(string='', readonly=True)

    def dummy_action_btn(self):
        return True
