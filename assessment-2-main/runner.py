
from curses.ascii import isalpha
from classes.customers import Customers
from classes.inventory import Inventory
from classes.video import Video
from classes.video_store import Video_store
from classes.customer import Customer
import csv

import os
script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
rel_path = "data/customers.csv"
cust_file_path = os.path.join(script_dir, rel_path)
rel_path="data/inventory.csv"
inv_file_path=os.path.join(script_dir, rel_path)
# Write your solution here!
my_store=Video_store()


with open(inv_file_path,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            my_store.inventory.add(Video(**row))

with open(cust_file_path,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            my_store.customers.add(Customer(**row))
            


while True:
    option=input("""== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View store customers
3. View customer rented videos
4. Add new customer
5. Rent video
6. Return video
7. Exit

Insert option here:""")
    
    if option=="1":
        print(f'{my_store.view_inventory()}')
    
    if option=="2":
        print(f'{my_store.view_customers()}')
    
    if option=="3":
        id=input('''Please enter the customers ID
ID:''')
    
        try:
            print(f'''
That customer has these titles checked out:
{my_store.customers.customers_list[id].get_video_rentals()}''')
    
        except: 
            print("This customer has no videos")
        
    if option=="4":
        new_cust_dict={}
        while True:
            new_cust_dict['first_name']=input("what is the customer's First Name?")
            if new_cust_dict['first_name'].isalpha():
                break
        while True:
            new_cust_dict['last_name']=input("what is the customer's Last Name?")
            if new_cust_dict['last_name'].isalpha():
                break
        while True:
            sp=input("type: s for standard account type: p for a premium account\n:")
            if sp== "s" or sp=="p":
                break
            else:
                print("s or p there are only 2 options here bucko")
        while True:
            xf=input("type: x for no restrictions type: f to get a family account\n:")
            if xf=="x" or xf=="f":
                break
            else:
                print("x or f are the only 2 options here pal")
        new_cust_dict['account_type']=sp+xf
        new_cust_dict['current_video_rentals']=""
        new_cust_dict['id']=int(list(my_store.customers.customers_list.keys())[-1])+1
        my_store.customers.add(Customer(**new_cust_dict))
        pass
    if option=="5":
        requested_video=input("what video would you like to rent?")
        id=input("enter your customer ID to checkout")
        my_store.customers.customers_list[id].rent(my_store.inventory,requested_video)
        
        pass
    if option=="6":
        requested_video=input("what video would you like to return?")
        id=input("enter your customer ID to return")
        my_store.customers.customers_list[id].return_video(my_store.inventory,requested_video)
        pass
    if option=="7":
        break


