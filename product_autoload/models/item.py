# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

_logger = logging.getLogger(__name__)

from openerp import api, models, fields


class Item(models.Model):
    """ El item se relaciona con el producto basado en el campo item_code
    """
    _name = 'product_autoload.item'

    item_code = fields.Char(
        help="Code from bulonfer, not shown"
    )
    name = fields.Char(
        help="Item name to show in category full name"
    )
    origin = fields.Char(
        help="where the product was made"
    )
    section_code = fields.Char(
        help="Code from bulonfer, not shown"
    )
    family_code = fields.Char(
        help="Code from bulonfer, not shown"
    )
    family_id = fields.Many2one(
        'product_autoload.family',
        ondelete='cascade',
        help="family to which the item belongs"
    )
    section_id = fields.Many2one(
        'product_autoload.section',
        ondelete='cascade',
        help='section to which the item belongs'
    )

    product_ids = fields.One2many(
        'product.product',
        'item_id',
        help="All products belonging to this item"
    )

    @api.model
    def unlink_data(self):

        # recorrer todos los productos y deslinkear las categorias
        for prod in self.env['product.template'].search([]):
            prod.categ_id = 1

        # eliminar todos los rubros, esto elimina en cascada
        # familias y secciones
        for item in self.env['product_autoload.item'].search([]):
            item.unlink()

            # eliminar todas las categorias
            # for cat in self.env['product.category'].search([('id', '!=', 1)]):
            #    cat.unlink()

    @api.model
    def link_data(self):
        item_obj = self.env['product_autoload.item']
        family_obj = self.env['product_autoload.family']
        section_obj = self.env['product_autoload.section']
        product_obj = self.env['product.product']

        # linkear todos los datos
        for item in item_obj.search([]):
            # linkear con familia
            family = family_obj.search(
                [('family_code', '=', item.family_code)])
            if not family:
                raise Exception('Item %s points to family %s but no family '
                                'record found in familia.csv', item.item_code,
                                item.family_code)

            item.family_id = family.id
            _logger.info('linked item %s with family %s', item.name,
                         family.name)

            # linkear con seccion
            section = section_obj.search(
                [('section_code', '=', item.section_code)])
            if not section:
                raise Exception('Item %s points to section %s but no section '
                                'record found in seccion.csv', item.item_code,
                                item.section_code)
            item.section_code = section.section_code
            _logger.info('linked item %s with section %s', item.name,
                         section.name)

            # linkear con productos
            product = product_obj.search(
                [('item_code', '=', item.item_code)]
            )
            if not product:
                raise Exception('No product found with idrubro=%s',
                                item.item_code)
            for prod in product:
                prod.item_id = item.id
                _logger.info('Linked product %s with item %s',
                             prod.default_code, item.item_code)

    @api.multi
    def create_categories(self):
        item_obj = self.env['product_autoload.item']
        family_obj = self.env['product_autoload.family']
        section_obj = self.env['product_autoload.section']
        product_obj = self.env['product.product']
        category_obj = self.env['product.category']

        for family in family_obj.search([]):
            categ = category_obj.search([('name', '=', family.name)])
            if not categ:
                category_obj.create({
                    'name': family.name
                })



