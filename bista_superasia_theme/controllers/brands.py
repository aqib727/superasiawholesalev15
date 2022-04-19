from odoo.http import request
from odoo import http


class WebsiteExtension(http.Controller):
    @http.route(['/brands'], type='http', auth="public", website=True, csrf=False)
    def brands(self, **post):
        return request.render('bista_superasia_theme.brands_page', {})
