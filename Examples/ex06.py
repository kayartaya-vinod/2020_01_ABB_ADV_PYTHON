from ex05 import Person

class Employee(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Person.__init__(self, **kwargs)
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary')

    @property
    def id(self): return self.__id

    @id.setter
    def id(self, value): self.__id = value

    @property
    def salary(self): return self.__salary

    @salary.setter
    def salary(self, value): self.__salary = value

    # override __str__ from Person
    def __str__(self):
        return 'Employee [id = {}, salary = {}, {}]'.format(
            self.id, self.salary, super().__str__())

    def __iadd__(self, value):
        if type(value) in (int, float):
            self.salary += value
        elif type(value) == str:
            self.name += value
        else:
            raise TypeError('Invalid type of value for +=')
        
        # all __iXXX__ functions should return self
        return self

    def __lt__(self, value):
        if type(value) == Employee:
            return self.salary < value.salary
        elif type(value) in (float, int):
            return self.salary < value
        else:
            raise TypeError('Invalid type of value for < operator')


def main():
    e1 = Employee(name='Ramesh', salary=45000, id=1234)
    e2 = Employee(name='Umesh', salary=55000, id=1234)
    # print('attributes of e1 are: ', dir(e1))
    print(e1) # invokes __str__ from Employee
    e1 += 5000 # want to add 5000 to e1.salary
    e1 += ' Kumar' # e1.name should become 'Ramesh Kumar'
    print(e1)

    print('e1 < 40000', e1 < 40000) # must compare e1.salary < 40000
    print('e1 < e2', e1 < e2)   # must compare e1.salary < e2.salary

if __name__=='__main__': main()

