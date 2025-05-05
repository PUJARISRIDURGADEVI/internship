# def student_gradebook():
#     limit=int(input("enter the no.of students: "))
#     for i in range(limit):
#         student_data={}
#         student_name=[]
#         student_rollno=[]
#         subject_wisemarks={}
#         name=input("enter the name of the student: ")
#         rollno=int(input("enter the roll no of the student: "))
#         student_name.append(name)
#         student_rollno.append(rollno)
#         for i in range(3):
#             subject=input("enter the subject name: ")
#             marks=int(input("enter the marks of the student: "))
#             subject_wisemarks[subject]=marks 
#         student_data['student_name']=student_name
#         student_data['student_rollno']=student_rollno
#         student_data['subject_wisemarks']= subject_wisemarks 
#         # student_data['subject_wisemarks'] = " / ".join(f"{subject}: {marks}" for subject, marks in subject_wisemarks.items())
#         student_data['total_marks']=sum(subject_wisemarks.values())
#         student_data['average_marks']=sum(subject_wisemarks.values())/len(subject_wisemarks)
#         if student_data['total_marks'] > 300:
#             grade='A'
#         elif student_data['total_marks'] > 250:
#             grade='B'
#         elif student_data['total_marks'] > 150:
#             grade='C'
#         else:
#             grade='fail'
#         student_data['grade']=grade
#         print(student_data)
#     sort=dict(sorted(student_data.items()))
#     print(sort)
#     name=input("Enter the name to search:")
#     if name in student_data:
#         search=student_data.get(student_name)
#         print(search)
#     else:
#         print(f'{student_name} not found')
# student_gradebook()
    



# def smart_grocery():
#     browser_items={}
#     cart={}
#     for i in range(2):
#         items=input("enter the name of items: ")
#         cost=int(input("enter cost of the items: "))
#         browser_items[items]=(cost)
#     while True:  
#         choice=input("Welcome to Smart Grocery!  \n 1. View Store Items\n 2. Add to Cart\n 3. View Cart\n 4. Remove Item\n 5. Checkout\n 6. Exit: ")
#         if choice=="1":
#             print(browser_items)
#         elif choice=="2":
#             items=input("enter add item to cart:")
#             if items in browser_items:
#                 quantity=int(input("enter quantity of the item: "))
#                 for i in range(quantity):
#                     cart[items]=browser_items.get(items)
#                     print(cart)
#             else:
#                 print(f"{items} not found")
#         elif choice=="3":
#                 print(cart)
#         elif choice=="4":
#             items=input("enter the item to remove from cart:")
#             if items in cart:
#                 cart[items]=cart.pop(items)
#                 print(cart)
#             else:
#                 print(f"{items} not found in cart")
#         elif choice=="5":
#             browser_items[items]=sum(cart.values()) 
#             print(f"your total bill is {browser_items[items]}")
#             print("thank you for shopping")              
#         elif choice=='6':
#             print('exit')
#             break
# smart_grocery()

def game():
    player=input("enter the character of the player: ")
    choice=input("1.room 2.room 3.room 4.room")
    health_coins=10
    items=[]
    explore_rooms()
def explore_rooms():
    if choice==1:
        action=input("here you have to fight wiṭh monster(fight/run)")
        if fight:
            fight=("fight with the monster with the help of sword/shield")
            if fight==sword/shield:
                print("you win  and having more coins and move to next room")
                health_coins+=2
            else:
                health_coins-=2
                print("you lose the coins")
        elif run:
            print("you run away from the monster and enter into next room")

    if choice==2:
        items=input("here pick up the items")
        for items in range(0,4):
            if items==4:
                print("")
        
    
game()
        