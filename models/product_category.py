
from odoo import fields, models


class ProductCategory(models.Model):

    _inherit = 'product.category'

    is_low_stock_alert = fields.Boolean(
        string="Low Stock Alert",
        help='This field determines the minimum stock quantity at which a low '
             'stock alert will be triggered.When the product quantity falls '
             'below this value, the background color for the product will be '
             'changed based on the alert state.')
    min_low_stock_alert = fields.Integer(
        string='Alert Quantity', default=0,
        help='Change the background color for the product based'
             'on the Alert Quant.')
