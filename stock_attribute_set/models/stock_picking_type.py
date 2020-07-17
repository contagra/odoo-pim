from odoo import fields, models


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    attribute_set_id = fields.Many2one(
        "attribute.set",
        "Default Attribute Set",
    )
