# def fact():
#     n=int(input("enter a number: "))
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print(fact())

from functools import reduce
n=int(input("enter a number: "))
factorial=lambda n:reduce(lambda x,y:x*y ,range(1,n+1),1)
print(factorial(n))
