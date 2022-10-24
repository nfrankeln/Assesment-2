class Customers:
    def __init__(self):
        self.customers_list=dict()
        pass
    def add(self,customer):
        if customer.id not in self.customers_list.keys():
            self.customers_list[f'{customer.id}']=customer