# -*- coding: utf-8 -*-
# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, models
from odoo.fields import first


class MassEditingWizard(models.TransientModel):
    _inherit = "mass.editing.wizard"

    @api.model
    def _get_field_options(self, field):
        res = super(MassEditingWizard, self)._get_field_options(field)
        if field.ttype == "many2one":
            attributes = self.env["attribute.attribute"].search(
                [("field_id", "=", field.id)]
            )
            attribute = first(
                attributes.filtered(lambda a: a.attribute_type == "select")
            )
            if attribute:
                res.update({"domain": "[('attribute_id', '=', %s)]" % attribute.id})

        return res
