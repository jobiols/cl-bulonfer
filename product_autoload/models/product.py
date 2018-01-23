# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def autoload(self):
        print 'hellooo- --------------------------'
