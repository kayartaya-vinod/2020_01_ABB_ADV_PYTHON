'''
Different ways to read files
'''
import sys

filename = './ex01.py'

def readfile_method1():
    f = open(filename, mode='rt')
    content = f.read() # reads the entire file and returns the content
    print(content)
    f.close()

def readfile_method2():
    f = open(filename)
    # f.readlines() returns a list consiting of all lines from the file
    for line in f.readlines():
        print(line, end='')
    f.close()
    
def readfile_method3():
    with open(filename) as f:
        # you may treat the file object 'f' as a genrator of lines of the file
        for line in f:
            print(line, end='')


#  python3 ex09.py 1

def main():
    # list of methods
    methods = [readfile_method1, readfile_method2, readfile_method3]
    try:
        if __name__!='__main__':
            choice=int(input('Enter a choice: '))
        else:
            choice = int(sys.argv[1])
        methods[choice-1]()
    except IndexError:
        print("Choice should be 1, 2, or 3")
    except ValueError:
        print('Choice must be a number')

if __name__=='__main__': main()