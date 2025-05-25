from odoo import models

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    def action_create_payments(self):
        res = super().action_create_payments()
        for payment in self.filtered(lambda p: p.journal_id.type in ['cash', 'bank']):
            sign = 1 if payment.payment_type == 'inbound' else -1

            self.env['account.bank.statement.line'].create({
                'date': payment.payment_date,
                'payment_ref': payment.communication or 'No Ref',
                'partner_id': payment.partner_id.id or False,
                'amount': sign * payment.amount,
                'foreign_currency_id': payment.currency_id.id or False,
                'amount_currency': sign * payment.amount if payment.currency_id else 0.0,
                'journal_id': payment.journal_id.id,
                'company_id': payment.company_id.id,
            })
        return res
