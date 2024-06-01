from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm_and_create_deliveries(self):
        self.action_confirm()

        # Group order lines by product
        product_lines = {}
        for line in self.order_line:
            if line.product_id in product_lines:
                product_lines[line.product_id]['quantity'] += line.product_uom_qty
            else:
                product_lines[line.product_id] = {
                    'line': line,
                    'quantity': line.product_uom_qty,
                }

        # Create deliveries
        for product, details in product_lines.items():
            self._create_delivery(details['line'], details['quantity'])

    def _create_delivery(self, sale_order_line, quantity):
        stock_picking = self.env['stock.picking'].create({
            'partner_id': self.partner_id.id,
            'picking_type_id': self.warehouse_id.out_type_id.id,
            'location_id': self.warehouse_id.lot_stock_id.id,
            'location_dest_id': self.partner_id.property_stock_customer.id,
            'origin': self.name,
        })

        self.env['stock.move'].create({
            'name': sale_order_line.name,
            'product_id': sale_order_line.product_id.id,
            'product_uom_qty': quantity,
            'product_uom': sale_order_line.product_uom.id,
            'location_id': self.warehouse_id.lot_stock_id.id,
            'location_dest_id': self.partner_id.property_stock_customer.id,
            'picking_id': stock_picking.id,
            'sale_line_id': sale_order_line.id,
            'state': 'draft',
        })

        stock_picking.action_confirm()
        stock_picking.action_assign()
