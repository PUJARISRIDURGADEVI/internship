# # print statements ---- used to print statement
# print("hello world")
# print("write whatever you want in quotes only")
# # types
# # --custom words(dev[user define])
# # --key words(def,print,int,if,else,for etc...)



<<<<<<< HEAD
# input statements
a=input("write a number")
b=input("write a alphabet")
=======
# # input statements
# a=input("write a number")

# continous prime numbers
# for num in range(1,11):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 print(f"{num} is not prime")
#         else:
#             print(f"{num} is prime")

# for num in range(2,101):
#     is_prime=True
#     for i in range(2,num-1):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(num)

# sentence="hell0 how are you"
# lit=sentence.split(",")
# print(lit)
# count={}
# for i in lit:
#     if i in count:
#         count[i] = count[i]+1
#     else:
#         count[i]=1
# for key,value in count.items():
#     print(key,":",value)


# def is_palindrome(s):
#     return s==s[::-1]
# s="devi"
# print(is_palindrome(s))


# input=50
# num1=12
# num2=input-num1
# if num1!=num2:
#     print("the two different numbers:",num1 , "and" ,num2)
# else:
#     print("the numbers are not different")


nums=[-2,1,-3,4,-1,2,2,-5,4]
max_sum=nums[0]
current_sum=num[0]
start=end=0
s=0
for i in range(1,len(nums)):
    if nums[i] > current_sum + nums[i]:
        current_sum=nums[i]
        s=i
    else:
        current_sum += nums[i]
        
    if current_sum > max_sum:
        max_sum = current_sum
        start=s
        end=i
return (max_sum, nums[start:])

def non_repeated_chr(str):
    for chr in str:
        if str.count(chr)==1:
            return chr
    return none
str="abcdafbdsfdfg"
print(non_repeated_chr(str))
>>>>>>> 6f7cd761f5911cb1c76a65068848f46a96663f04
