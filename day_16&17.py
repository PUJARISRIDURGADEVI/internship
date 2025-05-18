# class Dog:
#     # This is a class
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#     def sample(self):
#         print(self.name,self.breed)
#     def pratice(self):
#         print(self.name)
# my_dog = Dog("Bruno", "Labrador")
# my_dog.sample()
# my_dog.pratice()

# def add(a,b):
#     print(a+b)
# add(3,4)

# class cal:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print(self.a+self.b)
#     def sub(self):
#         print(self.a-self.b)
# answer=cal(2,3)
# answer.add()
# answer.sub()


# class student:
#     def __init__(self,name,roll_no,marks=0):
#         self.name=name
#         self.roll_no=roll_no
#         self.marks=marks
#     def add_marks(self):
#         sub_marks=[]
#         for i in range(3):
#             add_marks=int(input("enter the marks: "))
#             sub_marks.append(add_marks)
#             self.marks=sub_marks
#     def calculate_total(self):
#         return sum(self.marks)
#     def calculate_average(self):
#         return sum(self.marks)/len(self.marks)
#     def display_report(self):
#         total_marks=self.calculate_total()
#         average=self.calculate_average()
#         print(f"name:{self.name},roll_no:{self.roll_no},marks:{self.marks},total:{total_marks},average:{average}")
# grade_book=student("john",34)
# grade_book.add_marks()
# grade_book.display_report()


# class book:
#     def __init__(self,title,author,avaliability):
#         self.title=title
#         self.author=author
#         self.avaliability=avaliability 
#     def borrow(self):
#         title=input("enter the title: ")
#         if title == self.title:
#             print(f"{self.title} is available")
#         else:
#             print("title as not avaliable")
#     def return_book(self):
#         title=input("enter the title: ")
#         if title==self.title:
#             print(f"{self.title} has been returned")
#         else:
#             print("as not borrow")

#     def display(self):
#         print(f"title:{self.title},author:{self.author},{self.avaliability}")
# library_book=[book("data science","joel gurs","avaliability"),book("java","sun microsystem","avaliability")]
# for book in library_book:
#     book.display()
# book.borrow()
# book.return_book()
# book.display()
        
class car:
    def __init__(self,brand,model,price,available):
        self.brand=brand
        self.model=model
        self.price=price
        self.available=available
    def sell(self):
        name=input("enter the brand: ")
        if name!= self.brand:
            print("not available")
        else:
            print("available")
    def display(self):
        print(f"brand:{self.brand},model:{self.model},price:{self.price},available")
my_car=car("audi","Q3",44.99,"available")
my_car.sell()
my_car.display()