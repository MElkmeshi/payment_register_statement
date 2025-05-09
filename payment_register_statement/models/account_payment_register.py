from odoo import models

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    def action_create_payments(self):
        res = super().action_create_payments()
        # create statement lines for cash journals
        for payment in self.filtered(lambda p: p.journal_id.type == 'cash'):
            statement_line = self.env['account.bank.statement.line'].create({
                'date': payment.payment_date,
                'payment_ref': payment.communication or 'No Ref',
                'partner_id': payment.partner_id.id or False,
                'amount': payment.amount,
                'foreign_currency_id': payment.currency_id.id or False,
                'amount_currency': payment.amount if payment.currency_id else 0.0,
                'journal_id': payment.journal_id.id,
                'company_id': self.env.company.id,
            })
            statement_line.action_save_close()
        return res
