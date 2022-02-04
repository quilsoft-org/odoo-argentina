# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields


class AccountInvoiceReport(models.Model):

    _inherit = 'account.invoice.report'

    company_currency_id = fields.Many2one('res.currency', string='Company Currency', readonly=True)  # change label
    invoice_currency_id = fields.Many2one('res.currency', string='Invoice Currency', readonly=True)
    line_id = fields.Many2one('account.move.line', string='Journal Item', readonly=True)
    price_unit = fields.Monetary('Unit Price', readonly=True, currency_field='invoice_currency_id',)
    discount = fields.Float('Discount (%)', readonly=True)
    discount_amount = fields.Monetary(
        'Discount Amount', readonly=True, group_operator="sum", currency_field='invoice_currency_id',)

    amount_total = fields.Monetary(string='Untaxed Total', currency_field='invoice_currency_id', readonly=True)

    # por ahora no lo agregamos, el que teniamos ya era en moneda de cia y basicamente el nuevo price_subtotal ya lo
    # hace
    # price_subtotal_signed = fields.Monetary(
    #     'Subtotal (Inv. Currency)', help='Subtotal amount on invoice currency and signed (refunds are negative)',
    #     readonly=True, group_operator="sum", currency_field='invoice_currency_id',)
    # por ahora no lo sumamos
    # price_gross_subtotal

    # use monetary field instead of float
    # amount_total = fields.Monetary()
    # price_subtotal = fields.Monetary()
    # price_average = fields.Monetary(group_operator="avg")

    _depends = {'account.move': ['currency_id'], 'account.move.line': ['price_unit', 'discount']}

    def _select(self):
        return super()._select() + """,
            line.price_unit,
            line.id as line_id,
            move.currency_id AS invoice_currency_id,
            line.price_total * currency_table.rate *
                (CASE WHEN move.move_type IN ('in_refund','out_refund','in_receipt') THEN -1 ELSE 1 END)
            AS amount_total,
            line.discount,
            line.price_unit * line.quantity * line.discount/100 *
                (CASE WHEN move.move_type IN ('in_refund','out_refund','in_receipt') THEN -1 ELSE 1 END) as discount_amount
            """

    def _group_by(self):
        return super()._group_by() + ", move.currency_id"
