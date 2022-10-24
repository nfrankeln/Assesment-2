from classes.video import Video
import csv


class Inventory:
    def __init__(self):
        self.inventory_stock=dict()

    def add(self,item):
        if item.title not in self.inventory_stock.keys():
            self.inventory_stock[f'{item.title}']=item
    
    def checkout(self,title):
        try:    
            if self.inventory_stock[f'{title}'].copies_available > 0:
                    self.inventory_stock[f'{title}'].decrement_copies()
                    return title
            else:
                print("There are no copies available to rent")
        except:
            print("No such title in our inventory")
    
    def check_in(self,title):
        self.inventory_stock[f'{title}'].increment_copies()
        return title
    
    # def return_movie(self,movie_title):
    #         self.inventory_stock[f'{movie_id}'].rent



