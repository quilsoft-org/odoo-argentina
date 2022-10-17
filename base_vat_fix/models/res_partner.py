# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, tools, _
from odoo.exceptions import Warning
class ResPartner(models.Model):
    _inherit = 'res.partner'


    """TODO: esta solucion no es la mejor pero provisoriamente es lo mejor q se pudo ahcer"""
    @api.constrains('vat', 'country_id')
    def check_vat(self):
        try:
            super(ResPartner, self).check_vat()
        except:
            if self.vat not in [self.country_id.l10n_ar_natural_vat,
                                self.country_id.l10n_ar_legal_entity_vat,
                                self.country_id.l10n_ar_other_vat]:
                raise Warning("VAT invalido, por favor revise los VAT por paises y asegurese de poner correctamente  el valor.")