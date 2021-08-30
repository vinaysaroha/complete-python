mylist = [1,2,3]
print(len(mylist))

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self): # to print instance of the class
        return f"{self.title} by {self.author} has {self.pages} pages"

    def __len__(self):
        return self.pages
mybook = Book('python','vinay',100)
print(f"book {mybook.title} is written by {mybook.author} has {mybook.pages} pages")
print(mybook)
print(str(mybook))
print(len(mybook))

