{
    'name':'Avantgarde Theme',
    'description': 'Avantgarde is a sophisticated theme to inspire and impress',
    'category': 'Theme/Creative',
    'summary': 'Arts, Galleries, Trends, Shows, Magazines, Blogs',
    'sequence': 150,
    'version':'1.1.0',
    'author':'Odoo S.A.',
    'data': [
        'views/assets.xml',
        'views/customize_modal.xml',
        'views/snippets.xml',
        'views/options.xml',
        'views/images_library.xml'
        ],
    'demo': [
        'demo/demo-data.xml',
        'demo/style.xml',
        'demo/welcome.xml',
        'demo/artgallery.xml',
        'demo/magazine.xml',
        'demo/art_shop.xml',
        'demo/blocks.xml'
    ],
    'images': [
        'static/description/poster.jpg',
        'static/description/avantgarde_screenshot.jpg',
    ],
    'depends': ['theme_common', 'snippet_google_map'],
    'price': 199,
    'currency': 'EUR',
    'live_test_url': 'https://theme-avantgarde.odoo.com',
}
