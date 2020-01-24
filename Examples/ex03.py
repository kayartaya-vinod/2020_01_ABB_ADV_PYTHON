'''
Object oriented basics in Python

To create a class use the 'class' keyword

Ex:

class Person:
    # code

To create an object:

p1 = Person()

'''

class Person:
    def __init__(self):
        print('got id(self) as', id(self))
        
    def print(self):
        print('inside print, got id(self) as', id(self))

def main():
    p1 = Person() # using the class as a function
    print('type of p1 is', type(p1))
    print('id of p1 is', id(p1))
    p1.print()
    # Person.print(p1)


if __name__=='__main__': main()
