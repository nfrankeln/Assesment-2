from classes.person import Person
from classes.inventory import Inventory
from classes.account import Account
class Customer(Person,):
    def __init__(self,**kwargs):
        super().__init__(kwargs['first_name'],kwargs['last_name'])
        self.account_type=Account(kwargs['account_type'][0],kwargs['account_type'][1])
        self.current_video_rentals=self.current_video_rentals_setter(kwargs['current_video_rentals'])
        self.id=kwargs['id']
        pass
    
    def current_video_rentals_setter(self,input):
        if input=="":
            return []
        else:
            return input.split('/')
        pass
    def get_video_rentals(self):
        #output=self.current_video_rentals.replace('/','\n')
        output=""
        for video in self.current_video_rentals:
            output+=f'{video}\n'
        return output
    
    def rent(self,inventory,video_title):
        #if current video rentals<account allowance and #movie not violate account restriction
        if self.account_type.amount<len(self.current_video_rentals)+1:
            print("""
    Account Limit Reached!!! Try returning some movies first""")
        #and self.account_type.restrictions != inventory.inventory_stock[f'{video_title}'].rating:
        elif self.account_type.restriction == inventory.inventory_stock[f'{video_title}'].rating:
           print("\nYour account does not allow you to rent this movie")
        else:
            self.current_video_rentals.append(inventory.checkout(video_title))
    def return_video(self,inventory,video_title):
        self.current_video_rentals.remove(inventory.check_in(video_title))
    def customer_display(self):
        return f'First Name: {self.first_name}\nLast Name: {self.last_name} \nid: {self.id}\n--------------\n'

