# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class HRTimesheetSubmitAccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    submitted = fields.Boolean(string='Submitted')

    @api.model
    def mark_submitted(self, domain):
        for aal in self.env['account.analytic.line'].search(domain):
            aal.sudo().submitted = True
        return True

    @api.model
    def check_submitted_validated(self, domain):
        for aal in self.env['account.analytic.line'].search(domain):
            if not aal.submitted and aal.validated or not aal.submitted and not aal.validated:
                return True
        return False

    @api.multi
    def action_validate_timesheet_warning(self):
        if self:
            employees_names = []
            for aal in self:
                if aal.submitted is False and aal.employee_id.name not in employees_names:
                    employees_names.append(aal.employee_id.name)

            if employees_names:
                return self.env['account.analytic.line.validate.warning'].with_context(self_ids=self.ids)\
                    .warning(message='\n'.join(employees_names))
            else:
                return self.action_validate_timesheet()
        else:
            return self.action_validate_timesheet()





