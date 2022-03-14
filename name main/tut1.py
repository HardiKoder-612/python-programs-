"""if i don't write write main statement, tut2 will also execute the line 9 of tut1 thats why to prevent this, we use main as the content defined inside it will not get imported in another (tut2) file"""
def statement(str):
    print(f"The statement is {str}")

def add(a,b):
    return (a+b+5)

if __name__ == '__main__':
    statement("Hardik is a good boy")
    print(add(4,6))
