class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.city = kwargs.get('city', '')

    def __str__(self):
        return 'Person [Name = {}, City = {}]'.format(
            self.__name, self.__city)

    @property
    def name(self): return self.__name

    # you can create a setter for 'name',
    # only if there is a @property for 'name'
    @name.setter
    def name(self, value): 
        if type(value) != str: raise TypeError('Name must be a str')
        if len(value)>0 and len(value) <3: raise ValueError('Name must have at least 3 letters')
        self.__name = value

    @property
    def city(self): return self.__city

    @city.setter
    def city(self, value): 
        if type(value) != str: raise TypeError('City must be a str')
        self.__city = value

def main():
    p1 = Person(name='Vinod', city='Bangalore')
    p2 = Person(city='Dallas', name='John')

    print(p1)
    print(p2)

    # this looks like a value assignment, but it invokes the member
    # function (@name.setter) by supplying (p1, 'Vinod Kumar') as args
    p1.name = 'Vinod Kumar'
    p1.city = 'Shimoga'
    print(p1)

if __name__=='__main__': main()
