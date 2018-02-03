# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

_logger = logging.getLogger(__name__)

from openerp import api, models, fields


class Family(models.Model):
    """ Una Familia es un conjunto de rubros
    """
    _name = 'family'

    item_ids = fields.One2many(
        'item',
        'family_id')

    name = fields.Char(
        help="Name of family to show in category full name"
    )

