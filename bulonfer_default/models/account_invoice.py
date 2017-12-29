# -*- coding: utf-8 -*-

from openerp import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.model
    def add_invoices(self):
        """
        Agrega una factura y sus lineas,
        se requiere:
            company
            partner
            journal
            y las dos cuentas
        """

        partner = self.env['res.partner'].search([('name', '=', 'ADHOC SA')])
        account = self.env['account.account'].search([('code', '=', '101200')])
        journal = self.env['account.journal'].search([('code', '=', 'INV')])
        company = self.env['res.company'].search([('name', '=', 'Exento')])
        values = {
            'state': 'draft',
            'partner_id': partner.id,
            'account_id': account.id,
            'journal_id': journal.id,
            'company_id': company.id,
        }
        invoice_id = self.create(values)
        # import wdb;wdb.set_trace()

        account = self.env['account.account'].search([('code', '=', '200000')])
        invoice_line = self.env['account.invoice.line']
        values = {
            'invoice_id': invoice_id.id,
            'product_id': 61,
            'price_unit': 100,
            'account_id': account.id,
            'name':'pedor'
        }
        invoice_line.create(values)

        print '>>>>>>>>>>>>>>>>>>>>>>>', invoice_id



