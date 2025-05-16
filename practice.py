# for i in range(4,0,-1):
#   a=" "*(4-i)
#   b=" * "*(i)
#   print(a+b)

# for i in range(1,5,1):
#   a=" "*(5-2*(i))
#   b=n" * "*(i)
#   print(a+b)
# for j in range(4,0,-1):
#   a="  "*(4-j)
#   b=" * "*(j-1)
#   print(a+b)

# for i in range(1,6,1):
#   if i==1 or i==5:
#     print(" * "*5)
#   else:
#     print(" * "+"   "*(3)+" * ")
# n=5
# for i in range(2,n+1,1):
#   if i==1 or i==4:
#     print(" * "*5)
#   else:
#     print(" * "+"   "*(3)+" * ")

# n=4
# for i in range(1,5):
#   if i==1:
#     print(" "*(n-i)+"*")
#   else:
#     print(" "*(n-i)+"*"+" "*(2*(i)-3)+"*")
# for j in range(3,0,-1): 
#   if(j==1):
#     print(" "*(n-j)+"*")
#   else:
#     print(" "*(n-j)+"*"+" "*(2*(j)-3)+"*")

# for i in range(1,4,1):
#   i="1"*i
#   print(i)
# n=5
# for i in range(1,n+1,1):
#   for j in range(i):
#     print(i, end=" ")
#   print()


# n = 5
# for i in range(1, n + 1): 
#   a = " " * (n - i)        # Outer loop for rows
#   for j in range(i):           # Inner loop for elements in each row
#     print(a + str(i), end="") # Combine spaces and the row number
#   print()  

def console_app():
    stored_items={}
    limit=int(input("enter the no of items: "))
    try:
        for i in range(limit):
            items=[]
            items_names=input("enter the item names: ")
            items_price=float(input("enter the item price: "))
            items_quantity=int(input("enter the quantity of the item: "))
            items.append(items_price)
            items.append(items_quantity)
            stored_items[items_names]=items  
    except ValueError:
        print("negative quantity") 
    print("\n view stored  items: ")
    print(stored_items)
    return make_purchase()
def make_purchase():
    items_names=input("enter a item name to purchase: ")
    quantity_needed=int(input("purchase item quantity needed:"))
    for items_names in stored_items:
        if items_quantity>=quantity_needed:
            print("purchase sucessfully!")
        elif items_quantity<quantity_needed:
            print("stock is not avaliable")
        else:
            print("item not found")
console_app()