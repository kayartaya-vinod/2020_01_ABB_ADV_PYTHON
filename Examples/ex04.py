'''
class Person with member attributes
'''

class Person:
    def __init__(self, name, city='Bangalore'):
        # add members to self 
        self.__name = name
        self.__city = city

    def print_info(self):
        print('Name = %s' % (self.__name))
        print('City = %s' % (self.__city))

    # this function textually represents an object
    def __str__(self):
        return 'Person [Name={}, City={}]'.format(self.__name, self.__city)

def main():
    p1 = Person('Vinod', 'Bengaluru')
    p1.print_info()
    print(p1) # equivalent of print(p1.__str__())
    print(dir(p1))
    p1.__name = 1234 # does not affect the 'private' __name attribute in p1
    print(p1)

if __name__=='__main__': main()
