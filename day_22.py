# def fact():
#     n=int(input("enter a number: "))
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print(fact())

# from functools import reduce
# n=int(input("enter a number: "))
# factorial=lambda n:reduce(lambda x,y:x*y ,range(1,n+1),1)
# print(factorial(n))

# my_list=[1,2,3,4,5,6,7,8,9]
# prime_num=list(filter(lambda x : all(x%i!=0, range(2,x),my_list)))
# print(prime_num)

# list_of_tuples=[("Amit", 85), ("Neha", 92), ("Raj", 78)]
# sort_list=sorted(list_of_tuples,key=lambda x:x[1])
# print(sort_list)

# names=["john", "alice", "mohit"]
# title_case=list(map(lambda x:x.title(),names))
# print(title_case)

# my_list=[121,342,12321,34,929,141,45,2]
# palindrome_list=list(filter(lambda x:str(x)==str(x)[::-1],my_list))
# print(palindrome_l


# my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# squares=list(map(lambda x:x**2,my_list))
# even_num=list(filter(lambda x:x %2 ==0,squares))
# print(even_num)

# from functools import reduce
# my_list=[1,3,5,8,9]
# max_num=reduce(lambda x,y :x if x>y else y,my_list)
# print(max_num)

# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# operation=input("enter a operation: +, -, *, /: ")
# calculator={: lambda a,b:a+b,}