# -*- coding: utf-8 -*-
#
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

#     is_frozen = fields.Boolean('Frozen Item', default=False)

    unit_barcode = fields.Char('Unit Barcode')

    _sql_constraints = [
        ('unit_barcode_uniq', 'unique(unit_barcode)', 'A Unit barcode can only be assigned to one product !')]

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    purchase_order = fields.Char('Purchase Order#')

class AccountMove(models.Model):
    _inherit = 'account.move'

    purchase_order = fields.Char('Purchase Order#')
