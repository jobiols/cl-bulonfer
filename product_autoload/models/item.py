# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

_logger = logging.getLogger(__name__)

from openerp import api, models, fields


class Item(models.Model):
    """ El item se relaciona con el producto basado en el campo item_code
    """
    _name = "item"

    name = fields.Char(
        help="Item name to show in category full name"
    )
    origin = fields.Char(
        help="where the product was made"
    )
    family_id = fields.Many2one(
        'family',
        help="family to which the item belongs"
    )
    section_id = fields.Many2one(
        'section',
        help='section to wich the item belongs'
    )

    product_ids = fields.One2many(
        'product.product',
        'item_id',
        help="All products belonging to this item"
    )
