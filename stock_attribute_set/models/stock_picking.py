from odoo import api, fields, models


class Picking(models.Model):
    """The mixin 'attribute.set.owner.mixin' override the model's fields_view_get()
    method which will replace the 'attributes_placeholder' by a group made up of all
    the stock.picking's Attributes.
    Each Attribute will have a conditional invisibility depending on its Attribute Sets.
    """

    _inherit = ["stock.picking", "attribute.set.owner.mixin"]
    _name = "stock.picking"

    attribute_set_id = fields.Many2one(
        "attribute.set",
        "Attribute Set",
        default=lambda self: self._get_default_att_set(),
    )

    def _get_default_att_set(self):
        """ Fill default attribute_set with its picking type's default attribute_set."""
        if self.picking_type_id and self.picking_type_id.attribute_set_id:
            return self.picking_type_id.attribute_set_id.id

    @api.onchange("picking_type_id")
    def onchange_picking_type_id(self):
        self.ensure_one()
        if self.picking_type_id and (
                not self.attribute_set_id or self.attribute_set_id and self.attribute_set_id.model_id.model == self._name):
            self.attribute_set_id = self.picking_type_id.attribute_set_id
