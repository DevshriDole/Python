class Book:
    title=" "
    author=" "
    year=" "
    available=True
    
    def __init__(self,title,author,year,available):
        self.title=title
        self.author=author
        self.year=year
        self.available=available
        #Book.available=False
    def display_details(self):
        print(f'Title of book is:{self.title} \nAuthor of book is:{self.author} \nYear of release {self.year} \nAvailability of book is {self.available}' )
book1=Book("It ends with us","Collen Hover",2021,True)
book2=Book("It starts with us","Collen Hover",2024,True)
#book1.available=False
book1.display_details()
book2.display_details()
