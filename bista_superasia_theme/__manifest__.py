
{
    'name': "SuperAsia Website Theme",
    'version': '13.0.1.0.0',
    'category': 'Website',
    'summary': 'SuperAsia Website Theme.',
    'description': """SuperAsia Website Theme.""",
    'author': "Bista Solutions Pvt. Ltd.",
    'website': 'www.bistasolutions.com',
    'license': 'AGPL-3',
    # "depends": ['base','web','website','portal','bista_web_pwa','superasiab2b_b2c','sale','payment','website_sale','website_form','auth_signup','website_sale_delivery','website_sale_stock','sale_stock','website_crm'],
    # TODO: purchase dependecy missing
        "depends": ['base','web','website','portal', 'product', 'sale','payment','website_sale','auth_signup','website_sale_delivery','website_sale_stock','sale_stock','website_crm'],
    "data": [
        'security/ir.model.access.csv',
        # 'views/assets.xml',
        'views/webclient_template.xml',
        'views/homepage_template.xml',
        'views/header_footer_inherit.xml',
        'views/shop_page_inherit.xml',
        'views/product_page_inh.xml',
        # 'views/cart_page_inherit.xml',
        # 'views/contact_us_template_inherit.xml',
        # 'views/portal_template.xml',
        'views/company.xml',
        # 'views/gta_code.xml',
        # 'views/delivery_carrier.xml',
        # 'views/check_postal_code.xml',
        'views/product_template.xml',
        # 'views/sale_order.xml',
        'data/data.xml', # NOTE: From website_extension module
        'views/brands_page.xml', # NOTE: From website_extension module
        #'views/pricelist_view.xml', # NOTE: From website_extension module
        'views/product_attribute.xml', # NOTE: From website_extension module
    ],

    "installable": True,
    "application":True,
    'assets': {
        'web.assets_frontend': [
            'bista_superasia_theme/static/src/scss/mdb.min.css',
            # 'bista_superasia_theme/static/src/vendor/bootstrap/css/bootstrap.min.css',
            'bista_superasia_theme/static/src/vendor/bootstrap/css/bootstrap-grid.min.css',
            'bista_superasia_theme/static/src/vendor/icofont/icofont.min.css',
            'bista_superasia_theme/static/src/vendor/boxicons/css/boxicons.min.css',
            'bista_superasia_theme/static/src/vendor/animate.css/animate.min.css',
            'bista_superasia_theme/static/src/vendor/venobox/venobox.css',
            'bista_superasia_theme/static/src/vendor/aos/aos.css',
            'bista_superasia_theme/static/src/scss/style.css',
            
            'bista_superasia_theme/static/src/js/typed.min.js',
            # 'bista_superasia_theme/static/src/vendor/jquery-sticky/jquery.sticky.js',
            'bista_superasia_theme/static/src/vendor/counterup/counterup.min.js',
            'bista_superasia_theme/static/src/vendor/aos/aos.js',
            'bista_superasia_theme/static/src/vendor/jquery.easing/jquery.easing.min.js',
            'bista_superasia_theme/static/src/vendor/venobox/venobox.min.js',
            'bista_superasia_theme/static/src/vendor/waypoints/jquery.waypoints.min.js',
            'bista_superasia_theme/static/src/vendor/isotope-layout/isotope.pkgd.min.js',
            'bista_superasia_theme/static/src/js/website_sale.js',
            'bista_superasia_theme/static/src/js/custom_js.js',
            # 'bista_superasia_theme/static/src/js/feature_products.js',
            'bista_superasia_theme/static/src/js/main.js',


        ]
    }
}
