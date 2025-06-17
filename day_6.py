person={'name':'devi','age':22,'gmail':'devipujari.com','address':'galayagudem'}
print(person)
person['add']='eluru'
print(person)
numbers={1,1,3,2,6,2,2}
print(numbers)
numbers.add(10)
print(numbers)
numbers.remove(2)
print(numbers)
n=11 
for   i in range(2,11):
    if n%i==0:
        print(f'n is not prime')
else:
    print('is a prime')  


countdown=10
secret_code=[5]
while countdown>0:
    seconds=int(input(f"count down the number from 10 to 1 timeleft {countdown}: "))
    if seconds==secret_code:
        print("bomb is defused")
        break
    else:
        print("Wrong code! Decreasing the countdown by 2 seconds.")
        countdown -= 2 
print("bomb is exploded")


student_gradebook={}
for i in range(0,5):
    name=input("enter the name: ") 
    marks=int(input("enter the marks: "))
    student_gradebook[name]=marks
    print(student_gradebook)
if name in student_gradebook:
    name=input("enter the name: ")   
    print(student_gradebook.get(name))
    print(student_gradebook.keys())
    print(student_gradebook.values())
    print(student_gradebook.items())
    name=input("enter the name: ") 
    marks=int(input("enter the marks: "))
    student_gradebook.update({name:marks})
    print(student_gradebook)
    name=input("enter the name: ") 
    student_gradebook.pop(name)
    print(student_gradebook)
name=input("enter the name: ")
if name in student_gradebook:
   print("valid student name")
else:
   print("invalid student name")



unique_travellog=set()
for i in range(0,2):
    city=input("enter the name of the city that visited by the user: ")
    unique_travellog.add(city)
    print(unique_travellog)
city=input("enter the city:")
if city in unique_travellog:
    print("this city is already visited by the user")
else:
    unique_travellog.add(city) 
    print(unique_travellog) 
friends_history=set()
for i in range(0,2):
    city=input("enter the name of the city that visited by the user friend: ")
    friends_history.add(city)
    print(friends_history)
combine=unique_travellog.union(friends_history)
print("combination of the both cites: ",combine)
common=unique_travellog.intersection(friends_history)
print(common)
unique=unique_travellog.difference(friends_history)
print(unique)





        