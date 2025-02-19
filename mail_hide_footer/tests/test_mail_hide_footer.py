# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo_test_helper import FakeModelLoader

from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestMailFooter(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.loader = FakeModelLoader(cls.env, cls.__module__)
        cls.loader.backup_registry()
        from .models import ModelWithHideFooter

        cls.loader.update_registry((ModelWithHideFooter,))
        cls.partner = cls.env["res.partner"].create(
            {"name": "Test Partner", "email": "test@example.com"}
        )
        cls.test_record = cls.env["model.with.hide.footer"].create(
            {"partner_id": cls.partner.id}
        )
        cls.test_model = cls.env["ir.model"].search(
            [("model", "=", "model.with.hide.footer")], limit=1
        )

    @classmethod
    def tearDownClass(cls):
        """Restore registry after tests."""
        cls.loader.restore_registry()
        super().tearDownClass()

    def _send_test_email(self):
        self.test_record.message_post(
            body="Test email content",
            partner_ids=[self.partner.id],
            subtype_xmlid="mail.mt_comment",
            mail_auto_delete=False,
        )
        mail = self.env["mail.mail"].search(
            [("model", "=", self.test_model.model)], limit=1
        )
        return mail.body_html

    def test_email_footer_included(self):
        email_body = self._send_test_email()
        self.assertIn(
            "Sent",
            email_body,
            "The email footer should be present when `hide_email_footer` is disabled.",
        )

    def test_email_footer_hide(self):
        self.test_model.hide_email_footer = True
        email_body = self._send_test_email()
        self.assertNotIn(
            "Sent",
            email_body,
            "The email footer should be hidden when `hide_email_footer` is enabled.",
        )
