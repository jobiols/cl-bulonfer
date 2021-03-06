# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'Bulonfer',
    'version': '9.0.0.1.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customización Bulonfer SA',
    'author': 'jeo Software',
    'depends': [
        'base',
        'support_branding_jeosoft',
        'account_accountant',  # permisos para contabilidad

        # aplicaciones instaladas
        'price_security', 'price_security_fix',  # Quien ve el precio de costo
        'l10n_ar_aeroo_stock',
        'stock',
        'product_unique',
        'product_multi_barcode',
        'stock_picking_auto',  # Automatic picking when Invoice is validated.
        'account_fix',  # Account Fixes
        'product_autoload',
        # 'odoo2odoo',
    ],

    'data': [
        'data/config_data.yml'
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '80',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-bulonfer', 'branch': '9.0'},
        {'usr': 'jobiols', 'repo': 'cl-iomaq', 'branch': '9.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '9.0'},

        {'usr': 'oca', 'repo': 'connector', 'branch': '9.0'},
        {'usr': 'jobiols', 'repo': 'connector-odoo2odoo', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'connector-ecommerce', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'connector-prestashop', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'bank-payment', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'product-attribute', 'branch': '9.0'},
        {'usr': 'oca', 'repo': 'product-variant', 'branch': '9.0'},
    ],
    'docker': [
        {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '9.5'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
    ]

}
