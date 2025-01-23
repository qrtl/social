# Copyright 2025 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models
import logging

class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.model_create_multi
    def create(self, values_list):
        messages = super().create(values_list)
        for message in messages:
    
            if not (
                message.model == self._resource_model()
                and message.subtype_id
                and not message.subtype_id.internal
            ):
                continue
            logging.info("hjelo______")
            resource = self.env[self._resource_model()].browse(message.res_id)
            logging.info("Resoucre_______________")
            logging.info(resource)
            if getattr(resource, self._remain_state_field()) == self._remain_state_value():
                continue
            user = message.author_id.user_ids[:1]
            # if user and user.has_group("base.group_user"):
            #     continue
            parent = resource[self._parent_field()]
            logging.info("Parent_____________-")
            logging.info(parent)
            reply_stage = getattr(parent, self._reply_stage_field())
            if reply_stage:
                resource.sudo().write({'stage_id': reply_stage.id})
                continue
            reply_stage_id = int(
                self.env["ir.config_parameter"]
                .sudo()
                .get_param(self._config_key(), 0)
            )
            if reply_stage_id in getattr(parent, 'type_ids').ids:
                resource.sudo().write({'stage_id': reply_stage_id})
        return messages
    
    def _resource_model(self):
        """Override this method in child models to specify the model name."""
        raise NotImplementedError("Subclasses must implement `_resource_model`.")

    def _remain_state_field(self):
        """Override this method in child models to specify the remain state."""
        raise NotImplementedError("Subclasses must implement `_remain_state_field`.")
    
    def _remain_state_value(self):
        """Override this method in child models to specify the remain state value."""
        raise NotImplementedError("Subclasses must implement `_remain_state_value`.")

    def _reply_stage_field(self):
        """Override this method in child models to specify the reply stage field name."""
        raise NotImplementedError("Subclasses must implement `_reply_stage_field`.")

    def _parent_field(self):
        """Override this method in child models to specify the parent field name."""
        raise NotImplementedError("Subclasses must implement `_parent_field`.")

    def _config_key(self):
        """Override this method in child models to specify the config parameter key."""
        raise NotImplementedError("Subclasses must implement `_config_key`.")
