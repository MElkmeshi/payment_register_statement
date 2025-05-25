import logging
from odoo import models

_logger = logging.getLogger(__name__)

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_post(self):
        _logger.info("action_post override for payment IDs: %s", self.ids)

        res = super().action_post()

        for payment in self:
            _logger.info("Posting payment %s (journal type: %s)", payment.id, payment.journal_id.type)

            if payment.journal_id.type not in ['cash', 'bank']:
                continue

            sign = 1 if payment.payment_type == 'inbound' else -1

            self.env['account.bank.statement.line'].create({
                'date': payment.date,
                'payment_ref': payment.name or 'No Ref',
                'partner_id': payment.partner_id.id or False,
                'amount': sign * payment.amount,
                'foreign_currency_id': payment.currency_id.id or False,
                'amount_currency': sign * payment.amount if payment.currency_id else 0.0,
                'journal_id': payment.journal_id.id,
                'company_id': payment.company_id.id,
            })

        return res
