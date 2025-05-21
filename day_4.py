# for i in range(3):
#     i='*'
#     print(i)
# rows=int(input("enter the number of rows: "))
# for i in range(1,rows + 1):
#     spaces=(rows - i)*""
#     stars=" *" * (1*i - 1)
#     print(spaces + stars)

# rows=int(input("enter the number of rows: "))
# for i in range(rows,0,-1):
#     spaces= (rows - i)*" "
#     stars=" * " * (1*i)
#     print(spaces + stars)
    

 #5
# 
# secret=5
# guess=0
# while guess!=secret:
#     guess=int(input("guess the number between 1 and 10: "))
# if guess==secret:
#    print("your correct")
# else:
#    print("your wrong")
      
    
# secret_code="1234"
# for seconds in range(10,0,-1):
#    print("enter the number of seconds:" ,seconds)
#    a=int(input("enter the secret code: "))
#    if a==secret_code:
#       print("bomb is defused")
#    else:
#       print("bomb is exploded") 
#       break


# die=5
# i=0
# while i!=die:
#    i=int(input("enter the number: "))
# if i==die:
#    print("you win")
# else:
#    print("you lose")  







# for i in range(1,11,1):
#     print(i)

# i=1
# while i<=10:
#    print(i)
#    i+=1


# my_list=[1,2,3,4,5]
# sum=0
# for i in range(len(my_list)):
#     sum+=my_list[i]
# print(sum)


# n=int(input("enter the number: "))
# sum=0
# i=1#
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)


# n=int(input("enter the number: "))
# for i  in range(1,n+1):
#     if i%2==0:
#         print(i)
# for j in range(1,n+1):
#     if j%2!=0:
#         print(j)   

# n=int(input("enter the  number: "))
# i=1
# j=1
# while i<=n:
#     if i%2==0:
#        print(i) 
#     i+=1    
# while j<=n:
#     if j%2!=0:
#         print(j)
#     j+=1


# n=int(input("enter the number: "))
# for i in range(1,10):
#     for j in range()



# 65-91 ascii values for A to Z
# 97-123 ascii values for a to z


# row=int(input("enter the number of rows: "))
# alphabets=65 
# for i in range(1,row + 1):
#     spaces="  "*(row-i)
#     letters=(chr(alphabets)  + "  ") *i
#     alphabets+=1
#     print(spaces+letters)

# 



# rows=int(input("enter the number: "))
# alphabets=65
# for i in range(1,rows+1):
#     print("  " * (rows-i),end='')
#     for j in range(i):
#         print(f" {chr(alphabets)} ",end='')
#         alphabets+=1
#     print()


# rows=int(input("enter the number of rows: "))
# alphabets=ord('a')
# for i in range(1,rows+1):
#     print(" " * (rows-i),end='')
#     for j in range(i):
#         print(f" {chr(alphabets)} ",end='')
#         alphabets+=1
#     print()   

# fibanoicc
# n=int(input("enter the number: "))
# a=0
# b=1
# print(a,b,end='')
# for i in range(1,n+1):
#     sum=a+b
#     a=b
#     b=sum
#     print(f" {sum} ",end='')  

#  armstrong number

n=int(input("enter the number: "))
a=len(str(n))
sum=0
temp=n
while n>0:
    num=n%10
    num=num**a
    sum+=num
    n=n//10
if temp==sum:
    print("is armstrong")
else:
    print("not armstrong")


# secret_number=5
# guess=0
# while guess!=secret_number:
#     guess=int(input("enter the number between 1 to 10: "))
# if secret_number==guess:
#     print("right")
# else:
#     print("wrong")


# num=5
# atempts=5
# for i in range(1,atempts+1):
#     n=int(input("enter the gussing number(0-10): "))
#     if num==n:
#         print("guess is right")
#         break
#     else:
#         print(f"try again{atempts-i} atempts remaining")
# else:
#     print("your atempts are completed")

# n=int(input("enter the number: "))
# for i in range(2,n+1):
#     for j in range(i)
#     if i%2==0:
#         print("not prime")
#     else:
#         print("prime")



# for i in range(1,4):
#   i=" ***" 
#   print(i)