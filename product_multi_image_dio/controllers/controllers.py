# -*- coding: utf-8 -*-
# from odoo import http


# class ProductMultiImageDio(http.Controller):
#     @http.route('/product_multi_image_dio/product_multi_image_dio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_multi_image_dio/product_multi_image_dio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_multi_image_dio.listing', {
#             'root': '/product_multi_image_dio/product_multi_image_dio',
#             'objects': http.request.env['product_multi_image_dio.product_multi_image_dio'].search([]),
#         })

#     @http.route('/product_multi_image_dio/product_multi_image_dio/objects/<model("product_multi_image_dio.product_multi_image_dio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_multi_image_dio.object', {
#             'object': obj
#         })
