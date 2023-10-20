##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
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
##############################################################################
{
    "author": "ADHOC SA,Odoo Community Association (OCA), QUILSOFT",
    "website": "www.adhoc.com.ar",
    "license": "AGPL-3",
    "category": "Accounting & Finance",
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "wizard/res_config_settings_views.xml",
        "reports/report_withholding_certificate.xml",
        "views/account_payment_group_view.xml",
        "views/afip_tabla_ganancias_escala_view.xml",
        "views/afip_tabla_ganancias_alicuotasymontos_view.xml",
        "views/account_payment_view.xml",
        "views/res_partner_arba_alicuot_views.xml",
        "views/res_partner_view.xml",
        "views/account_tax_view.xml",
        "data/tabla_ganancias_data.xml",
        "data/account_tax_withholding_template.xml",
    ],
    "demo": [
        "demo/ir_parameter.xml",
    ],
    "depends": [
        "account_withholding_automatic",
        "l10n_ar_ux",
    ],
    "external_dependencies": {
        "python": ["pyafipws"],
    },
    "installable": True,
    "name": "Automatic Argentinian Withholdings on Payments",
    "version": "14.0.1.3.0",
}
