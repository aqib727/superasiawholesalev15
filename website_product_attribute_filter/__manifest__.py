{
    'name': 'Advanced Attribute Filters',
    'description': """
	Advanced Attribute Filters helps to improve the customer experience on your odoo store.
	Your customers love to find their desired products and choose products collection to save their time.
	Categorty Attributes, attribute groups , product feature , group features , 
	Website Sale Category For Attribute ,Website Product Features , Product Filter , Product Attribute
	""",
    'summary': 'Advanced Attribute Filters',
    'category': 'Website',
    'version': '15.0.1.0.0',
    'license': 'OPL-1',
    'author': 'Bista Solutions Pvt. Ltd.',
    'website': 'www.bistasolutions.com',
    'depends': ['website_sale_comparison', 'bista_superasia_theme'],
    'data': [
        'views/templates.xml'
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_frontend': [
            'website_product_attribute_filter/static/src/css/website_product_filter.css',

            'website_product_attribute_filter/static/src/js/attribute.js',

        ]
    }
}