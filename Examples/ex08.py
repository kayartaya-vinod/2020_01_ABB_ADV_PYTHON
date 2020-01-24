class NamesUtil:
    __names = [] # mutable object; shared across objects

    # this is equivalent to 'static' functions of Java, C#
    # must be invoked using class and not object
    def print_names():
        print(NamesUtil.__names)

    def __init__(self):
        # self.names is same as NamesUtil.names in this case
        # self.__names.extend(['Vinod', 'Kumar'])
        self.__names += ['Vinod', 'Kumar']

    def str__(self):
        return f'Names are {self.__names}'

    def add_name(self, name):
        self.__names.append(name)

def main():
    n1 = NamesUtil()
    n2 = NamesUtil()

    print(n1) # same as print(n1.__str__())
    print(n2)

    n1.add_name('Shyam')
    print(n2)
    NamesUtil.print_names()

if __name__=='__main__': main()
