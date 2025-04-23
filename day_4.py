# for i in range(3):
#     i='*'
#     print(i)
# rows=int(input("enter the number of rows: "))
# for i in range(1,rows + 1):
#     spaces=" " * (rows - i)
#     stars="*" * (2*i - 1)
#     print(spaces + stars)

# secret=5
# guess=int(input("guess the number between 1 and 10: "))
# while guess!=secret:
#     if guess<secret:
secret=5
guess=int(input("guess the number between 1 and 10: "))
while guess!=secret:
    if guess==secret:
      print("your correct")
    else:
      print("your wrong")
      break
