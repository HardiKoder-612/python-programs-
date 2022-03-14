class library:
    book=[]
    name=""
    def __init__(self,book,name):
        self.book=book
        self.name=name
        pass
    def displaybook(self):
        print("Following books are available at library->\n")
        for i in self.book.items():
            print(i,"\n")
        pass
    def addbook(self,bname):
        self.book.push(bname)
        print(("Book Added"))
        pass
    def lendbook(self,bname):
        self.book.pop(bname)
        print("Book lend")
        pass
    def returnbook(self,bname):
        self.book.push(bname)
        print("Book returned")
        pass
