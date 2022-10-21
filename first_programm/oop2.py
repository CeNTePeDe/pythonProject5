class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}, salary = {self.salary}, bonus={self.bonus}%, ' \
               f'total bonus = {self.calculate_total_bonus()} rub'


class Cleaner(Employee):
    def __init__(self, name):
        super(Cleaner, self).__init__(name, salary=15000, bonus=1)


class Manager(Employee):
    def __init__(self, name):
        super(Manager, self).__init__(name, salary=45000, bonus=15)


class CEO(Employee):
    def __init__(self, name):
        super(CEO, self).__init__(name, salary=105000, bonus=100)

if __name__ == '__main__':
    masha = Cleaner('Maria Ivanovna')
    print(masha)
    grisha = Manager('Grigoriy Petrovich')
    print(grisha)
    ivan_palych = CEO('Ivan Pavlovich')
    print(ivan_palych)
