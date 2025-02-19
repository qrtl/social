# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _notify_record_by_email(
        self,
        message,
        recipients_data,
        msg_vals=False,
        model_description=False,
        mail_auto_delete=True,
        check_existing=False,
        force_send=True,
        send_after_commit=True,
        **kwargs
    ):
        model = msg_vals.get("model") if msg_vals else message.model
        if model:
            model_obj = (
                self.env["ir.model"].sudo().search([("model", "=", model)], limit=1)
            )
            if model_obj.hide_email_footer:
                self = self.with_context(hide_mail_footer=True)
        return super()._notify_record_by_email(
            message,
            recipients_data,
            msg_vals=msg_vals,
            model_description=model_description,
            mail_auto_delete=mail_auto_delete,
            check_existing=check_existing,
            force_send=force_send,
            send_after_commit=send_after_commit,
            **kwargs
        )
