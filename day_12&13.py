# def mul():
#     rows=int(input("enter the no of rows: "))
#     colums=int(input("enter the no of colums: "))
#     for i in range (rows):
#         for j in range(colums):
#             print(f"{i*j:4}",end='')
#         print()
# mul()

try:
    name=input("enter the name: ")
    # print(names)
    print(f"{names}")
except NameError:
    print("invalid error")


rows=4
columns=5
for i in range(1,rows+1):
    for j in range(1,columns+1):
        print(f"{i*j:4}", end='')       
    print()


rows=int(input("enter number of rows: "))
columns=int(input("enter number of columns:"))
matrix=[]
for i in range(1,rows+1):
    rows=[]
    for j in range(1,columns+1):
        rows.append(i*j)
    matrix.append(rows)
for rows in matrix:
    for elements in rows:
        print(f"{elements:4}",end='')
    print()
n=5
for j in range(1,n+1):
    a=" " * (n-j)
    print(str(a)+"* "*j)
for i in range(4,0,-1):
    a=" " * (n-i)
    print(str(a)+"* " *i)

def grid():
    rows=int(input("enter number of rows: "))
    columns=int(input("enter number of columns:"))
    matrix=[]
    for i in range(1,rows+1):
        rows=[]
        for j in range(1,columns+1):
            rows.append(i*j)
        matrix.append(rows)
    for rows in matrix:
        for elements in rows:
            print(f"{elements:4}",end='')
        print()
    guess_row=int(input("guess the row between (0-4)"))
    guess_col=int(input("guess the column between(0-4)"))
    correct_ans=abs(guess_row)+abs(guess_col)
    if correct_ans>3:
        print("too far!")
    elif correct_ans==2:
        print("getting warmer!")
    else:
        print("you got the treasure")
grid()

try:
    num=int(input("enter the number: "))
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
except ValueError:
    print("invalid num ")

def cal():
    try:
        num1=int(input("enter the number1: "))
        num2=int(input("enter the number2:  "))
        operators=input("enter the given operators:(+,-,<,>,**): ")
        if operators =='+':
            print(num1+num2)
        elif operators =='-':
            print(num1-num2)
        elif operators =='<':
            print(num1<num2)
        elif operators =='>':
            print(num1>num2)
        elif operators=='**':
            print(num1**2)
        else:
            print("invalid operator")
    except ValueError:
        print("please enter valid integer")
cal()

try:
   choose=input("Choose a wire to cut (red/blue/green): ")
   if choose=="red":
    print("danger")
   elif choose=="blue":
    print("no danger, but not safe")
   elif choose=="green":
    print("safe")
   else:
    raise ValueError("invalid color")
except ValueError:
    print("oops!Are you trying to invent new wires?")
