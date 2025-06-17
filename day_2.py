a=0.25
b="hello"
c=-1.25
d=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))

a=input("enter a number")
b=input("enter a number")
c= int(a)+int(b)
v=int(a)-int(b)
g=int(a)*int(b)     
h=int(a)/int(b)
print("a and b",c)
print(f"the sum of {a} and {b} is {c}")
print(f"the difference of {a} and {b} is {v}")
print(f"the product of {a} and {b} is {g}")
print(f"the division of {a} and {b} is {h}")


a=input("enter your birth year")
current_year=2025
age=current_year-int(a)
print(age)
forest=input("enter the number of coins to collect in forest: ") 
lake=input("enter the number of coins to collect in lake: ")
castle=input("enter the number of coins to collect in castle: ")
total_coins=int(forest)+int(lake)+int(castle)
print("total coins collected are",total_coins)

