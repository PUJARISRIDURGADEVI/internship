# name="devi"
# # print("hello,{}!".format(name))
# name="durga"
# age=20
# print("hi  %s  and age %d " %(name,age))

# character="player"
# print(f"welcome {character}")


# def conversation():
#     character_A="sai"
#     character_B="kiran"
#     print(f"hello {character_B} ,how are you?")
#     print(f"hey hi {character_A},yeah! fine")
#     print(f"how did you come here{character_B}")
#     print(f"i am going to my office in this way{character_A} ,then y are you here")
#     print(f"my house is near  by this way{character_B}")
#     print(f"ohh! okay {character_A}, then lets meet later and have a nice day")
#     print(f"yeah! {character_B} good to see you bye bye!!!!")
# conversation()


# my_list=[x**0.5 for x in range(5) ]
# print(my_list)

# a=3
# b=4
# c=a%b 
# # print(c)

# sentence=input("enter the sentence: ")
# my_list=[len(word) for word in sentence.split()]
# print(my_list)

# square=[x**2 for  x in range(1,11)]
# print(square)

# cube=[x**3 for x in range(1,11)]
# print(f"cubic numbers{cube}")

# even=[x for x in range(0,10) if x%2==0]
# odd=[x for x in range(0,10) if x%2!=0]
# print(even,odd)

prime=[x for x in range(2,10)  if all(x%j!=0 for j in range(2,x))]
print(" prime numbers", prime)

# def fibanoic():
#     num=[n , a:=0 , b:=1 for i in range(0,10) (sum=a+b a=b b=sum)]
#     print(f"{sum}" end='')
# fibanoic()