class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color
    
    def bark(self):
        print('woof')
    
    def run(self):
        print('Running')
# End of the class

dog = Dog()
dog.bark()
dog.run()

class Funds:
    total_expenses = 0
    total = 0
    error = ''

    def __init__(self, total):
        self.total = total

    def set_expense(self, expense):
        if self.get_funds_left() > expense:
            self.total_expenses += expense
            return True
        self.error = 'Out of Funds'
        return False

    def get_funds_left(self):
        return self.total - self.total_expenses
    
    def get_error(self):
        return self.error
        
funds = Funds(20)

if not funds.set_expense(10):
    print(funds.get_error())

if not funds.set_expense(2):
    print(funds.get_error())

if not funds.set_expense(15):
    print(funds.get_error())

print('You have $' + str(funds.get_fund_left()) + ' left.')


class Cycles:
    def set_as_assembled(self, is_assembled):
        self.assembled = is_assembled
    def get_wheel_count(self):
        return self.wheel_count
    def who_am_i(self):
        return 'I am the original function'
    
class Monocycke(Cycles):
    def who_am_i(self):
        return 'I am overriding the parent function'

class Bicycle(Cycles):
    wheel_count = 2

class Tricycle(Cycles):
    wheel_count = 3

monocycles = Monocycle()
print(monocycles.get_wheel_count())

cycles = Bicycle()
print(cycles.get_wheel_count())

print(monocycles.who_am_i())
print(cycles.who_am_i())