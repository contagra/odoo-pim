# Copyright 2020 Agrista GmbH (https://agrista.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Stock Attribute Set",
    "version": "13.0.1.0.1",
    "author": "Agrista GmbH",
    "website": "https://github.com/agrista/odoo-pim",
    "license": "AGPL-3",
    "category": "Operations/Inventory",
    "summary": "Allows display/editing of stock picking attributes in stock form views",
    "depends": ["attribute_set", "stock"],
    "data": ["views/attribute_attribute_views.xml", "views/stock_picking_type_views.xml", "views/stock_picking_views.xml"],
    "installable": True,
    'auto_install': False,
}
