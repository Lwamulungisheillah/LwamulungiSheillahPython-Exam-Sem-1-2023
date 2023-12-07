#NO.2(i)

class Book:
    def __init__(self,title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages
#an instance of a class        
instance= Book("Romeo and Juliet","Shakespeare",100)    
print(instance.title,instance.author,instance.pages)


# a function returning the title and its author        
class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        #an instance of a class        
    def myfunc(self):
      print(self.title,self.author,self)       
instance2= Book("Romeo and Juliet","Shakespeare")    
instance2.myfunc()

#a derived class to inherit the book class
# class EBook:
#     def __init__(self,Book):

#a class
#is a container of an object

#an object 
#is an instance of a class

  




