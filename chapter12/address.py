class Address():

    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""

home_address = Address()

home_address.name = "Max"
home_address.line1 = "Dorotheenstr 6"

work_address = Address()

work_address.name = "Maximilian"
work_address.line1 = "California Bay Area"

print("My home street is " + home_address.line1)
print("I work at " + work_address.line1)

print()

class Dog():
    def __init__(self, new_name):
        self.age = 0
        self.name = new_name
        print("A new Dog is born!")

    def bark(self):
        print("woof my name's " + self.name)

my_dog = Dog("Sam")

#my_dog.name = "Sam"
my_dog.age = 3

my_dog.bark()

print()

def give_money(person):
    person.money += 100

class Person():
    def __init__(self):
        self.name = ""
        self.money = 0

bob = Person()
bob.name = "Bob"
bob.money = 100

give_money(bob)
print(bob.money)

print()

class Cat():
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = 0

    def meow(self):
        print("MEEEOOW!")

jessy = Cat()
jessy.name = "jessy"
jessy.color = "grey"
jessy.weight = 3

jessy.meow()

print()

class Monster():
    def __init__(self):
        self.name = ""
        self.health = 0

tom = Monster()
tom.health = 180


def decrease_health(amount, monster):
    monster.health -= amount
    if monster.health < 0:
        print("monster died")

decrease_health(200, tom)

print(tom.health)