# class Vault:
#     def __init__(self,pin):
#         self.__pin=pin
#     def set_pin(self):
#         self.__pin=input("Enter a 4-digit pin: ")
#     def unlock(self):
#         unlock_pin=input("enter the pin to unlock")
#         if unlock_pin==self.__pin:
#             print("its open")
#         else:
#             print("pin is incorrect retry")
#     def lock(self):
#         print("vault is locked")
# a=Vault("1234")
# a.set_pin()
# a.unlock()
# a.lock()


# class Student:
#     def __init__(self,name,grade):
#         self.__name=name
#         self.__grades=[]
#     def add_grades(self):
#         n=int(input("Enter add grade to list: "))
#         self.__grades.append(n)  
#     def get_average(self):
#         return sum(self.__grades)/len(self.__grades)
#     def display_report(self):
#         print("name:",self.__name)
#         print("grades:",self.__grades)
#         print("average:",self.get_average())
# stu_grade=Student("john",10)
# stu_grade.add_grades()
# stu_grade.display_report()

# class Bankaccount:
#     def __init__(self,ba):
#         self.__ba=0
#     def deposit(self,amount):
#         if self.__ba<amount:
#             self.__ba+=amount
#     def with_draw(self,amount):
#         if self.__ba>amount:
#             self.__ba-=amount
#         else:
#             print("insuffient balance")
#     def display_report(self):
#         print(f"balance:{self.__ba}")
# bank=Bankaccount(0)
# bank.deposit(3000)
# bank.with_draw(500)
# bank.display_report()

class Animal:
    def make_sound(self):
        print("some generic animal sound")
class lion(Animal):
    def make_sound(self):
        print("roar")
class  elephant(Animal):
    def make_sound(self):
        print("trumpet")
class  monkey(Animal):
    def make_sound(self):
        print("chatter")
for Animal in [lion(), elephant(), monkey()]:
    Animal.make_sound()


# class Shape:
#     def area(self):
#         pass
# class Class(Shape):
#     def area(self):
#         print("area of circle = π × r²")
# class Rectangle(Shape):
#     def area(self):
#         print("area of rectangle = l × b")
# class triangle(Shape):
#     def area(self):
#         print("area of triangle = 1/2 × b × h")
# for shape in [Class(), Rectangle(), triangle()]:
#     shape.area()

# class Game:
#     def attack(self):
#         print("attacks")
# class  Archer(Game):
#     def attack(self):
#         print( "shoots an arrow")
# class  knight(Game):
#     def attack(self):
#         print("swings a sword")
# class Mage(Game):
#     def attack(self):
#         print("casts a spell")
# for Game in [Archer(), knight(), Mage()]:
#     Game.attack()


