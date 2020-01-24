"""
This is an example module, created by Vinod for a demo at ABB.

Contact:
Vinod Kumar K
https://vinod.co/
vinod@vinod.co

"""
from json import dump

AUTHOR_NAME = 'Vinod Kumar K'
AUTHOR_EMAIL = 'vinod@vinod.co'

def print_info():
    print('Author name: ', AUTHOR_NAME)
    print('Author email: ', AUTHOR_NAME)

def factorial(num = 5):
    ''' This is a factorial function (simple logic). 
    The function takes 0 or 1 argument, and returns the factorial of same. 
    For non numerics the function will raise an error.

    This can produce factorial for any big number!
    '''

    if type(num) not in (int, float):
        raise Exception('Invalid datatype, only numbers are allowed')
        # raise will take the control away from the function
        # and hence 'else' is not required

    f = 1
    while num>1:
        f *= num
        num -= 1
    return f

def line(symbol = '-', count = 80):
    print(symbol * count)
    
def dirr(obj):
    return [ at for at in dir(obj) if at[0] != '_' ]
    # return [ at for at in dir(obj) if at[:2] != '__' ]

def fibo(num = 10):
    # -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    a, b = -1, 1
    i = 1
    while i<=num:
        c = a + b
        yield c # control temporarily is returned to the user
        # when the user wants to continue, the function resumes from here
        a, b = b, c
        i += 1
        

# def csv2json(filename = None):
#     if filename==None:
#         filename = input('Enter the CSV filename to read from: ')
#     try:
#         with open(filename) as f:
#             header = f.readline().strip().split(',')
#             list = []
#             for line in f:
#                 values = line.strip().split(',')
#                 data = dict(zip(header, values))
#                 list.append(data)
#             with open(filename[:-3]+'json', 'wt') as outfile:
#                 dump(list, outfile, indent=3)
#                 print('json file generated')
#     except Exception as e:
#         print(f'There was an error: {e}')

def csv2json(filename = None):
    if filename==None:
        filename = input('Enter the CSV filename to read from: ')
    try:
        with open(filename) as f:
            header = f.readline().strip().split(',')
            list = [ 
                dict(zip(header, line.strip().split(',')))
                for line in f 
            ]
            
            with open(filename[:-3]+'json', 'wt') as outfile:
                dump(list, outfile, indent=3)
                print('json file generated')
    except Exception as e:
        print(f'There was an error: {e}')
    finally:
        print('It\'s done!')

def main():
    csv2json('people.csv')

if __name__=='__main__': main()
