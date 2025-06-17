def sucessfully():
    print("Successfully completed the task!")
    name=input("enter your name: ")
    print(f"hey you!{name}")
    return True
sucessfully()

def cal(a,b):
    c=a+b
    d=a-b
    return c,d
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
print(cal(a,b))

def cal1(a,b):
    if a<b:
        return a+b 
    elif a==b:
        return a*b
    else:
        return a-b
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
print(cal1(a,b))


ass ---->1
def num(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
a=int(input("enter any number to check even or odd: "))
print(num(a))


ass -->
def cal(a,b):
    if a+b:
        return a+b
    elif a - b:
        return a-b
    elif a*b:
        return a*b
    elif a%b:
        return a%b
    else:
        return invalid 
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
opt = input("Enter an operator: ,+,-,*,% ")
if opt == "+":
    print(cal(a,b))
elif opt == "-":
    print(cal(a,b))
elif opt == "*":
    print(cal(a,b))
elif opt =="%":
    print(cal(a,b))
else: 
    print("Invalid Operator")


def num(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact
n=int(input("enter the number: "))
print("factorial of n is :",num(n))

def password():
    limit=8
    list_add = input("Enter the password: ")
    if int(len(list_add))<limit:
        return 'weak'
    elif int(len(list_add))>limit:
        return 'strong'
    else:
        return 'okay okay'
print(password())


def lister():
    my_list = []
    limit = int(input("Enter the maximum number of items to add: "))
    
    list_add = input("Enter the items separated by commas: ")
    list_add = list_add.split(",")

    for item in list_add:
        if len(my_list) < limit:
            my_list.append(item.strip())
        else:
            print("Limit reached! Extra items ignored.")
            break

    print("Final List:", my_list)

print(lister())


def contactbook():
    contacts={}
    limit=int(input("enter the number of contacts you want to add: "))
    for i in range(limit):
       name=input("enter the contact name: ")
       number=int(input("enter the contact number: "))
       contacts[name]=number
    print(contacts)
    addition_contact=input("add  the contact name: ")
    if addition_contact in contacts:
        print("name is already exist")
    else:
        number=int(input("enter the contact number: "))
        contacts[addition_contact]=number
    print(contacts)
    if name in contacts:
        name=input("to search  the name: ")   
        print(contacts.get(name))
    name=input("to delete the contact name: ")
    print(contacts.pop(name))
    return contacts
contactbook()


def beach():
    print("You're at the beach. Choose your path:")
    choice = input("choose your path forest or mountain? ")
    if choice=='forest':
        print("you have to face the riddle challenge")
        return forest()
    elif choice=='mountain':
        print("you have to  guess the number")
        return mountain()
def forest():
    print("you have enter into forest")
    choice=input("enter your choice left or right: ")
    if choice=="left":
        print("you found the riddle challenge")
    else:
        print("you are lost in forest")
    puzzle_answer=input("jumbile the word:vide ")
    correct="devi"
    if correct==puzzle_answer:
        return treasure()
    else:
        print("you lost")

def mountain():
    print("you have enter into mountain")
    choice=input("enter your choice left or right: ")
    if choice=="left":
        print("you found the number guessing game ")
    else:
        print("you lost in the mountain")
    print("here you have some instructions,you have guess the number  within 10 sec ,it jump 2 sec for every wrong ans")
    hint=print("You must guess a number between 1 and 5.")
    countdown=10
    secret_number=[5]
    while countdown>0:
        seconds=int(input(f"count down the number from 10 to 1 timeleft {countdown}: "))
        if seconds in secret_number:
            return treasure()
        else:
            print("Wrong code! Decreasing the countdown by 2 seconds.")
            countdown -= 2 
    print("you lost")
def treasure(): 
    print("🎉 Congratulations! You found the treasure!")
beach()
 