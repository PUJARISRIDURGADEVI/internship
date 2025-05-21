n=5
num=1
for i in range(5,0,-1):
    for j in range(1,i+1):
        print((num),end='')
        num+=1
    print()


# list=["a","b","c","d"]
# print(list)
# list.append(1)
# print(list)

# list=[1,2,3,4,5]
# list.sort()
# print(list)
# list.reverse()
# print(list)
# list.insert(2,"apple")
# print(list)
# print(len(list))
# list.remove(2)
# print(list)
# print(list.count(4))
# list.pop(2)
# print(list)


# tuple=(1,23,45,35,69,1)
# print(tuple)
# print(tuple.count(45))

# my_tuple=(1,20,3,4,5,6,7,8,9)
# print(my_tuple)
# print(my_tuple.c ount(20))


# l=[]
# list_cout=int(input("enter the number of elements: "))
# for i in range(list_count):
#     elements=input("enter the element: ")

# bag=()
# items=int(input("enter the number of  items in bag: "))
# for i in range(items):
#     item=input("enter the item: ")
#     if  items<6:
#         print(f"{item} push the item in bag ")  
# else:
#     print("bag is full")
# element=input("after full the bag do you want to remove the item (Yes/No): ")
# if element=='yes':
#     remove=input("remove the item in bag ,enter item you want to remove in bag{item}")
#     print(f"{remove} remove the item in bag")
# else:
#     print(f"add an element")


# list=[1,2,3,4,5,67,8,9,10]
# secret_code=1
# for i in range(5):
#     list=int(input(f"guess the secret code in list{list}: "))
#     if list==secret_code:
#         print("bomb is defused")
#         break 
# else: 
#     print("bomb is over")          


# n=5
# num=1
# for i in range(1,5,1):
#     a=" "*(n-i)
#     print(a,end='')
#     for j in range(1,i+1):
#         print("",num,end='')
#         num+=1
#     print('')    

# n=5
# aplahbet=ord('A')
# for i in range(5,0,-1):
#     a=" "*(n-i)
#     print(a,end='')
#     for j in range(1,i+1):
#         print(f" {chr(aplahbet)}",end='')
#         aplahbet+=1
#     print('')  

# l=["a","b","c","d"]
# # print(type(l))
# # print(len(l))
# # print(l[0])
# # print(l[1])
# # print(l[-2])
# # print(l[-1])
# # print(l[1:2])
# # print(l[:])
# # print(l[-3:-1])
# # print(l[-3:])
# # print(l[:1])
# l.append('e')
# print(l)
# l2=['f','g']
# l.append(l2)
# print(l)
# l.insert()

# a=("mon","tue","wed")
# # print(type(t))
# # print(len(t))
# # print(t[0])
# # t1=("thu","fri")
# # print(t+t1)
# # print(t[0:3])
# # print(t[-1])
# # t=list(t)
# # print(type(t))
# # t.append("thu")
# # print(t)
# # t=tuple(t)
# # print(t)
# for i in a:
#     print(i)



# stack=[]
# while True:
#     cmd=input("""enter a command\n a.add an item to stack\n d.delete an item from stack\n v.print all stack items\n q.quit the program\n:""")
#     if cmd=="a":
#         item=input("enter the item")
#         stack.append(item)
#     elif cmd=="d":
#         stack.pop()
#     elif cmd=="v":
#         print(stack)
#     else:
#         print("not a vaid command")
