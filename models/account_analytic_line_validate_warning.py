# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountAnalyticLineValidateWarning(models.TransientModel):
    _name = 'account.analytic.line.validate.warning'

    title = fields.Text(string="Title", readonly=True)
    message = fields.Text(string="Message", readonly=True)

    @api.multi
    def message_action(self):
        self.ensure_one()
        res = {
            'name': 'Warning',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': self.env['ir.model.data'].xmlid_to_res_id(
                'hr_timesheet_submit.account_analytic_line_validate_warning_form'),
            'res_model': 'account.analytic.line.validate.warning',
            'domain': [],
            'context': self._context,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'res_id': self.id
        }
        return res

    @api.model
    def warning(self, message):
        record = self.create({'title': 'The following users have not yet submitted all timesheets for this period.',
                              'message': message})
        return record.message_action()

    @api.multi
    def validate_lines(self):
        aal = self.env['account.analytic.line'].browse(self._context['self_ids'])
        return aal.action_validate_timesheet()


