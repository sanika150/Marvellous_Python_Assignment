
class BookStore:
    NoOfBooks=0
    def __init__(self,Name,Author):
       
        self.Value1=Name
        self.Value2=Author
        BookStore.NoOfBooks =BookStore.NoOfBooks+1
        

    def Display(self):
        print(f"{self.Value1} by {self.Value2}.No of books:{BookStore.NoOfBooks}")
        
    
   
obj1 = BookStore("C Programming","Dennis Ritchie")
obj1.Display()
obj2 = BookStore("Linux System Programming","Robert Love")
obj2.Display()




