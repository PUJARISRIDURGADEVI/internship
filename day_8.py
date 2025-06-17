def student_gradebook():
    student=[]
    limit=int(input("enter the no.of students: "))
    for i in range(limit):
        student_data={}
        subject_wisemarks={}
        name=input("enter the name of the student: ")
        rollno=int(input("enter the roll no of the student: "))
        for i in range(3):
            subject=input("enter the subject name: ")
            marks=int(input("enter the marks of the student: "))
            subject_wisemarks[subject]=marks 
        student_data['student_name']=name
        student_data['student_rollno']=rollno
        student_data['subject_wisemarks']= subject_wisemarks 
        # student_data['subject_wisemarks'] = " / ".join(f"{subject}: {marks}" for subject, marks in subject_wisemarks.items())
        student_data['total_marks']=sum(subject_wisemarks.values())
        student_data['average_marks']=sum(subject_wisemarks.values())/len(subject_wisemarks)
        if student_data['total_marks'] > 300:
            grade='A'
        elif student_data['total_marks'] > 250:
            grade='B'
        elif student_data['total_marks'] > 150:
            grade='C'
        else:
            grade='fail'
        student_data['grade']=grade
        print(student_data)
    name=input("enter name to sort: " )
    sort=dict(sorted(student_data.items()))
    print(sort)
    search_name = input("\nEnter the name to search: ")
    found=False
    for name in student:
        if name['student_name'] == search_name:  
            print("Student found:", student)
            found=True
        else:
            print(f"{search_name} not found in the records.")
   
student_gradebook()
    



def smart_grocery():
    browser_items={}
    cart={}
    limit=int(input("enter the no of items: "))
    for i in range(limit):
        items=input("enter the name of items: ")
        cost=int(input("enter cost of the items: "))
        browser_items[items]=(cost)
    while True:  
        choice=input("Welcome to Smart Grocery!  \n 1. View Store Items\n 2. Add to Cart\n 3. View Cart\n 4. Remove Item\n 5. Checkout\n 6. Exit: ")
        if choice=="1":
            print(browser_items)
        elif choice=="2":
            items=input("enter add item to cart:")
            if items in browser_items:
                quantity=int(input("enter quantity of the item: "))
                for i in range(quantity):
                    cart[items]=browser_items.get(items)
                    print(cart)
            else:
                print(f"{items} not found")
        elif choice=="3":
                print(cart)
        elif choice=="4":
            items=input("enter the item to remove from cart:")
            if items in cart:
                cart[items]=cart.pop(items)
                print(cart)
            else:
                print(f"{items} not found in cart")
        elif choice=="5":
            browser_items[items]=sum(browser_items.values()) 
            print(f"your total bill is {browser_items[items]}")
            print("thank you for shopping")              
        elif choice=='6':
            print('exit')
            break
smart_grocery()

def play_game():
    player=input("enter the character of the player: ")
    choice=int(input("1.room 2.room 3.room: "))
    health_coins=10
    items=[]
    tokens=set()

    print("Current health coins:", health_coins)
    if health_coins >= 12:
        print("You have enough health coins to win the game!")
        print("You found the treasure! You win!")
        break
    elif health_coins <= 0:
        print("You've run out of health coins. Game Over!")
        break

    explore_rooms(choice, health_coins, items, tokens)
def explore_rooms(choice, health_coins, items, tokens):
    if choice==1:
        action=input("here you have to fight wiṭh monster(fight/run)")
        if action=="fight":
            fight=("fight with the monster with the help of sword/shield")
            if fight in sword:
                print("you win  and having more coins and move to next room")
                health_coins+=2
            else:
                health_coins-=2
                print("you lose the coins")
        elif run:
            print("you run away from the monster and enter into next room")

    elif choice==2:
        item=input("here pick up the items")
        items.append(item)
        if len(items) == 4:
            print("You collected all items! You gain more coins and move to the next room.")
            health_coins += 2
        else:
            health_coins-=2
            print("you lose the health coins. Move to next room")
        
    elif choice==3: 
        answer = input("Solve the riddle: What has to be broken before you can use it? ")
        if answer.lower() == "egg":
            print("Correct! You gain the token.")
            player["tokens"].add("token")
            health_coins += 2
        else:
            print("Wrong answer!")
            health_coins -= 2
            print("You lose the health coins. Move to next room.")
    return health_coins

    print("Game Over!")


play_game()
        


def play_game():
    player = input("Enter the character of the player: ")
    choice = int(input("1. room  2. room  3. room: "))
    health_coins = 10
    items = []
    tokens = set()
     print("Current health coins:", health_coins)
        if health_coins >= 10:
            print("You have enough health coins to win the game!")
            print("You found the treasure! You win!")
            return
        elif health_coins <= 0:
            print("You've run out of health coins. Game Over!")
            return

    print("Game Over!")

    explore_rooms(choice, health_coins, items, tokens)

def explore_rooms(choice, health_coins, items, tokens):
    if choice == 1:
        action = input("Here you have to fight with monster (fight/run): ")
        if action == "fight":
            sword = ("Pick up the sword or shield: ")
            fight_with = input("Fight with the monster using sword or shield: ")
            if fight_with == sword:
                print("You win and gain more coins and move to next room.")
                health_coins += 2
            else:
                health_coins -= 2
                print("You lose some coins.")
        elif action == "run":
            print("You run away from the monster and enter into the next room.")
        else:
            print("Invalid action.")

    elif choice == 2:
        item = input("Here, pick up the item: ")
        items.append(item)
        for items in range(4):
            if len(items) == 4:
                print("You collected all items! You gain more coins and move to the next room.")
                health_coins += 2
            else:
                health_coins -= 2
                print("You lose health coins. Move to next room.")

    elif choice == 3: 
        answer = input("Solve the riddle: What has to be broken before you can use it? ")
        if answer == "egg":
            print("Correct! You gain the token.")
            tokens.add("token")
            health_coins += 2
        else:
            print("Wrong answer!")
            health_coins -= 2
            print("You lose health coins. Move to next room.")
    else:
        print("Invalid choice. Please choose a valid room.")
        return

    print("Health coins:", health_coins)
    return health_coins
play_game()



def play_game():
    player = input("Enter the character of the player: ")
    choice = int(input("1. room  2. room  3. room: "))
    health_coins = 10
    items = []
    tokens = set()
    explore_rooms(choice, health_coins, items, tokens)

def explore_rooms(choice, health_coins, items, tokens):
    if choice == 1:
        action = input("Here you have to fight with monster (fight/run): ")
        if action == "fight":
            sword = input("Pick up the sword or shield: ")
            fight_with = input("Fight with the monster using sword or shield: ")
            if fight_with == sword:
                print("You win and gain more coins and move to next room.")
                health_coins += 2
            else:
                health_coins -= 2
                print("You lose some coins.")
        elif action == "run":
            print("You run away from the monster and enter into the next room.")
        else:
            print("Invalid action.")

    elif choice == 2:
        find_item= input("Here, pick up the item: ")
        if find_item=="silver":
            print("You collected all items! You gain more coins and move to the next room.")
            items.append("find_item")
            health_coins += 2
        else:
            health_coins -= 2
            print("You lose health coins. Move to next room.")

    elif choice == 3: 
        answer = input("Solve the riddle: What has to be broken before you can use it? ")
        if answer == "egg":
            print("Correct! You gain the token.")
            tokens.add("token")
            health_coins += 2
        else:
            print("Wrong answer!")
            health_coins -= 2
            print("You lose health coins. Move to next room.")
    else:
        print("Invalid choice. Please choose a valid room.")
        return

    print("Health coins:", health_coins)
    if health_coins >= 10:
        print("You have enough health coins to win the game!")
        print("You found the Treasure! You win!")
    else:
        print("Game Over!")
play_game()


def play_game():
    player=input("enter the character name: ")
    