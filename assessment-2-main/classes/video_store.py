from classes.inventory import Inventory
from classes.video import Video
from classes.customers import Customers
class Video_store:
    def __init__(self):
        self.inventory=Inventory()
        self.customers=Customers()
        pass
    def view_inventory(self):
        inv_str="\n"
        for id,video in self.inventory.inventory_stock.items():
            inv_str+=video.stock_display()
        return inv_str

    def view_customers(self):
        cust_str="\n"
        for id,customer in self.customers.customers_list.items():
            cust_str+=customer.customer_display()
        return cust_str