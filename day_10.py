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
# print(c)

sentence=input("enter the sentence: ")
my_list=[len(word) for word in sentence.split()]
print(my_list)