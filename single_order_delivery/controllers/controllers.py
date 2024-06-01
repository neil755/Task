# -*- coding: utf-8 -*-
# from odoo import http


# class SingleOrderDelivery(http.Controller):
#     @http.route('/single_order_delivery/single_order_delivery', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/single_order_delivery/single_order_delivery/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('single_order_delivery.listing', {
#             'root': '/single_order_delivery/single_order_delivery',
#             'objects': http.request.env['single_order_delivery.single_order_delivery'].search([]),
#         })

#     @http.route('/single_order_delivery/single_order_delivery/objects/<model("single_order_delivery.single_order_delivery"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('single_order_delivery.object', {
#             'object': obj
#         })
