# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ModelWithHideFooter(models.Model):
    _name = "model.with.hide.footer"
    _inherit = ["mail.thread"]

    partner_id = fields.Many2one("res.partner")
