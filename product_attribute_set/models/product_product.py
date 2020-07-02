from odoo import api, fields, models


class ProductProduct(models.Model):
    """The mixin 'attribute.set.owner.mixin' override the model's fields_view_get()
    method which will replace the 'attributes_placeholder' by a group made up of all
    the product.template's Attributes.
    Each Attribute will have a conditional invisibility depending on its Attriute Sets.
    """

    _inherit = ["product.product", "attribute.set.owner.mixin"]
    _name = "product.product"
