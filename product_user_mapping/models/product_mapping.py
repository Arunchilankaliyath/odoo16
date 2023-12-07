from odoo import models,fields


class ProductUserMapping(models.Model):
    _name = 'product.user.mapping'
    _description = 'Product user mapping'

    name = fields.Char(string='Index',required=True)
    user_ids = fields.Many2many('res.users', string='user')
class SaleOrder(models.Model):
    _inherit = 'sale.order'


    product_mapping_id = fields.Many2one('product.user.mapping', string='product')

class SalesOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_mapping_id = fields.Many2one('product.user.mapping', string='product')



