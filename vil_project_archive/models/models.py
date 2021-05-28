# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

class education_history(models.Model):
    _inherit = 'project.project'

    status = fields.Boolean('Status',default=False)


    def mark_archive(self):
        self.active = False
        return {
            'name': 'Projects',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'view_id': self.env.ref('project.view_project_kanban').id,
            'res_model': 'project.project',
            'type': 'ir.actions.act_window',
            'target': 'main',
        }
    def mark_active(self):
        self.active = True
        return {
            'name': 'Archived Projects',
            'view_type': 'kanban',
            'view_mode': 'kanban',
            'view_id': self.env.ref('project.view_project_kanban').id,
            'res_model': 'project.project',
            'type': 'ir.actions.act_window',
            'target': 'main',
            'domain': [('active','=',False)]
        }

