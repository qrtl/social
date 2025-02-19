# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class IrModel(models.Model):
    _inherit = "ir.model"

    hide_email_footer = fields.Boolean(
        help="If enabled, emails sent from records of this model will hide the "
        "email footer (Sent by [Company Name] using Odoo)."
    )
