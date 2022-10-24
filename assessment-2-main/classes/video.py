class Video():
    def __init__(self,**kwargs):
        self.id=kwargs['id']
        self.title=kwargs['title']
        self.rating=kwargs['rating']
        self.release_year=kwargs['release_year']
        self.copies_available=int(kwargs['copies_available'])
        pass
    
    def decrement_copies(self):
            self.copies_available-=1
    
    def increment_copies(self):
        self.copies_available+=1
    
    def stock_display(self):
        return f'Title: "{self.title}"\nCopies Available: {self.copies_available}\n------------------\n'




