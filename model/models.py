from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class invoice(models.Model):
    _name = 'account.move'
    _inherit = 'account.move'

    printer_data = fields.Text(string="Printer Data", required=False, readonly=True)


    def dummy(sef):
        pass


    def generate_printer_data(self):
        tpl = self.env['mail.template'].search([('name', '=', 'Dot Matrix Invoice')])
        data = tpl._render_template(tpl.body_html,'account.move', self.id, post_process=False)
        self.printer_data = data


    def action_invoice_cancel(self):
        self.printer_data=''
        return super(invoice, self).action_cancel()


    def action_invoice_open(self):
        res=super(invoice, self).action_invoice_open()
        if self.type=='out_invoice':
            self.generate_printer_data()
        return res







class purchase(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'

    printer_data = fields.Text(string="Printer Data", required=False, readonly=True)

    
    def dummy(sef):
        pass

    
    def generate_printer_data(self):
        tpl = self.env['mail.template'].search([('name', '=', 'Dot Matrix PO')])
        data = tpl._render_template(tpl.body_html, 'purchase.order', self.id, post_process=False)
        self.printer_data = data


    
    def button_confirm(self):
        res = super(purchase, self).button_confirm()
        self.generate_printer_data()
        return res


class picking(models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'

    printer_data = fields.Text(string="Printer Data", required=False, readonly=True)

    
    def dummy(sef):
        pass

    
    def generate_printer_data(self):
        tpl = self.env['mail.template'].search([('name', '=', 'Dot Matrix Picking')])
        data = tpl._render_template(tpl.body_html, 'stock.picking', self.id)
        self.printer_data = data


    
    def action_confirm(self):
        res = super(picking, self).action_confirm()
        #self.generate_printer_data()
        return res

    
    def action_cancel(self):
        res = super(picking, self).action_cancel()
        self.printer_data=''
        return res

class sale(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    printer_data = fields.Text(string="Printer Data", required=False, readonly=True)

    
    def dummy(sef):
        pass

    
    def generate_printer_data(self):
        tpl = self.env['mail.template'].search([('name', '=', 'Dot Matrix SO')])
        data = tpl._render_template(tpl.body_html, 'sale.order', self.id)
        self.printer_data = data

    
    def action_confirm(self):
        res = super(sale, self).action_confirm()
        self.generate_printer_data()
        return res

    
    def action_cancel(self):
        res = super(sale, self).action_cancel()
        self.printer_data=''
        return res

