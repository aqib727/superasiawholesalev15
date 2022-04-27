# -*- coding: utf-8 -*-
from odoo import fields, models, _
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    website_meta_ingredients = fields.Text("Website meta ingredients", translate=True)
    is_featured_product = fields.Boolean(string="Feature Product?",
                                         help="Check true if you want this product to be in Featured Products on E-commerce homepage.")

    # TODO: Will enable priority_sequence after confirmation
    # priority_sequence = fields.Integer('Website View Sequence', default=500,
    #                      help="Determine the display order in the Website E-commerce Shop Page \n Lowest value(1,2,3,4...) will show in top")

    # def _default_priority_sequence(self):
    #     self._cr.execute("SELECT MAX(priority_sequence) FROM %s" % self._table)
    #     max_sequence = self._cr.fetchone()[0]
    #     if max_sequence is None:
    #         return 500
    #     return max_sequence

    def featured_products_domain(self):
        return [('is_featured_product', '=', True)]
    
    def featured_products(self):
        main_list = []
        temp_list=[]

        domain = self.featured_products_domain()

        # if request.env.user.user_has_groups('base.group_public') or request.env.user.user_has_groups('superasiab2b_b2c.group_b2cuser'):
        #     domain.append(('is_hide_b2c', '=', False))
        # elif request.env.user.user_has_groups('superasiab2b_b2c.group_b2baccount'):
        #     domain.append(('is_hide_b2b', '=', False))

        prodids = self.env['product.template'].sudo().search(domain)
        # _logger.info('========prodids========= %s' % prodids)

        for prod in prodids:
            if len(temp_list) < 6:
                temp_list.append(prod)
            else:
                main_list.append(temp_list)
                temp_list=[]
                temp_list.append(prod)

        if temp_list:
            main_list.append(temp_list)
        # _logger.info('========main_list========= %s' % main_list)
        return main_list


    def _get_combination_info(self, combination=False, product_id=False, add_qty=1, pricelist=False, parent_combination=False, only_template=False):
        """Override for website, where we want to:
            - 

        """
        self.ensure_one()
        combination_info = super(ProductTemplate, self)._get_combination_info(
            combination=combination, product_id=product_id, add_qty=add_qty, pricelist=pricelist,
            parent_combination=parent_combination, only_template=only_template)
        if combination_info['product_id']:
            product = self.env['product.product'].sudo().browse(combination_info['product_id'])
            onhand_qty = product.qty_available # TODO: add more logic on onhandqty in future
            combination_info.update({
                'onhand_qty': int(onhand_qty),
                'avail_qty':int(product.qty_available),
                'updated_cart_qty':int(product.cart_qty),
                'product_uom': product.uom_id.name,
            })
        return combination_info