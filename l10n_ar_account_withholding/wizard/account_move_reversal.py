from odoo import models


class AccountMoveReversal(models.TransientModel):

    _inherit = "account.move.reversal"

    def reverse_moves(self):
        """ Forzamos fecha de la factura original para que el amount total de la linea
            se calcule bien
        """

        # TODO Hay que hacer QA con esto porque no se que implicaciones puede tener
        # en la v13 es self.move_id con lo que hay solo una factura y una fecha, aqui
        # manejan un conjunto de facturas. Estoy tomando la primera solamente para ver
        # que pasa pero no se que puede pasar si vienen varias facturas.

        date = self.move_ids[0].date
        self = self.with_context(invoice_date=date)
        res = super(AccountMoveReversal, self).reverse_moves()
        move_re = self.env['account.move'].browse(res.get('res_id'))
        move_re.sudo().write(
            {'l10n_ar_currency_rate': self.move_ids[0].l10n_ar_currency_rate})
        return res
