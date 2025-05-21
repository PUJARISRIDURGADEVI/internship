# class Vehicle:
#     def __init__(self,speed,capacity):
#         self.speed=speed
#         self.capacity=capacity
# class  Car(Vehicle):
#     def speed(self):
#         print(f"{self.speed} ")
#     def capacity(self):
#         print(f"{self.capacity}")
# class  Bus(Vehicle):
#     def speed(self):
#         print(f"{self.speed} ")
#     def capacity(self):
#         print(f"{self.capacity}")
# a=Car("40 ","4")
# b=Bus("50 kms",'20 members')
# a.speed()
# a.capacity()
# b.speed()
# b.capacity()  

# class Vehicle:
#     def __init__(self, speed, capacity):
#         self.speed = speed
#         self.capacity = capacity

# class Car(Vehicle):
#     def speed_info(self):
#         print(f"Speed: {self.speed}")

#     def capacity_info(self):
#         print(f"Capacity: {self.capacity}")

# class Bus(Vehicle):
#     def speed_info(self):
#         print(f"Speed: {self.speed}")

#     def capacity_info(self):
#         print(f"Capacity: {self.capacity}")

# # Create objects
# a = Car("40 km", "4 members")
# b = Bus("50 km", "20 members")

# # Call methods
# a.speed_info()
# a.capacity_info()
# b.speed_info()
# b.capacity_info()


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"name:{self.name},age:{self.age}")
# class student(person):
#     def study(self):
#         super().display()
# class teacher(person):
#     def teach(self):
#         super().display()
# s=student("john",20)
# a=teacher("jane",30)
# s.study()
# a.teach()    

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"name:{self.name},salary:{self.salary}")
class manager(employee):
    def calculate_salary(self):
        super().display()
class developer(employee):
    def calculate_salary(self):
        super().display()
a=manager("sai",30000)
b=developer("kiran",20000)
a.calculate_salary()
b.calculate_salary()


