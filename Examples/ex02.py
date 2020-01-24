'''
This is an example for working with different types of function arguments.

1. mandatory arguments
2. arguments with default values (optional arguments)
3. arbitrary arguments (*args)
4. keyword arguments (**kwargs)
'''
from ex01 import line

def test_fn1(name, city='Bangalore'): 
    '''
    name is the mandatory argument
    city is the optinoal argument, with default value of 'Bangalore'
    '''
    print('Name = ', name)
    print('City = ', city)
    line()


def average(*args):
    # print('args is', args)
    # print('type of args is', type(args))
    args = [n for n in args if type(n) in (int, float)]
    return sum(args) / len(args)

def test_fn2(**kwargs):
    # kwargs['name'] raises an exception KeyError if 'name' is not a valid key
    print('Name = ', kwargs.get('name'))
    print('Email = ', kwargs.get('email'))
    print('City = ', kwargs.get('city', 'Bangalore'))
    line()

def main():
    test_fn2(name='Vinod')
    test_fn2(name='Vinod', email='vinod@vinod.co')
    test_fn2(name='Vinod', city='Bengaluru')
    test_fn2(email='vinod@vinod.co', name='Vinod', city='Bengaluru')
    test_fn2()

def main_2():
    # average() takes variable length arguments
    avg = average(10, 20, 30, 'vinod', 'kumar', 100, 200)
    print('avg =', avg)

    avg = average(1,2,3,4,5,6,7,8,9,10)
    print('avg =', avg)

    line()

def main_1():
    # test_fn1() # this is an error, 'name' is missing
    test_fn1('Vinod')
    test_fn1('Vinod', 'Shivamogga')

    data = ('John', 'Dallas')
    test_fn1(data)
    test_fn1(*data) # strip the tuple/list content

    data = { 'name': 'Jane', 'city': 'Washington' }
    test_fn1(data)
    test_fn1(**data) # for dict, use ** and for list/tuple/set use *


# call the main() only if this module is run directly (and not imported)
if __name__=='__main__': main()