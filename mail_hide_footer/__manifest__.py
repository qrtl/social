# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Mail Hide Footer",
    "version": "15.0.1.0.0",
    "category": "Mail",
    "author": "Quartile, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/social",
    "depends": ["mail"],
    "license": "AGPL-3",
    "data": [
        "data/mail_template.xml",
        "views/ir_model_views.xml",
    ],
    "external_dependencies": {
        "python": ["odoo_test_helper"],
    },
    "installable": True,
}
