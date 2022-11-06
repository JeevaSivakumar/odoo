# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class product_multi_image_dio(models.Model):
#     _name = 'product_multi_image_dio.product_multi_image_dio'
#     _description = 'product_multi_image_dio.product_multi_image_dio'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
