class BookStore:
    NoofBooks=0

    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        BookStore.NoofBooks +=1

    def Display(self):
        print(self.Name,"by",self.Author,"No of Books",BookStore.NoofBooks)

obj1=BookStore("Linux system programming","Robert Love")
obj1.Display()

obj2=BookStore("C programming","Dennis Ritchie")
obj2.Display()
