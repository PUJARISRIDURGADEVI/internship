# # text="i am beginer in python course"
# # print(text.replace("beginer","beginning"))
# # print(text.split("i"))
# # def text():
# #     item_list=[]
# #     for i in range(5):
# #         items=input("enter the item name: ")
# #         item_list.append(items)
# #         print("_".join(item_list))
# #     print(item_list)
# # text()
# # def text1():
# #     a=input("enter something: ")
# #     print(a.split("/"))
# #     print(a)
# # text1()

# # def ass1():
# #     paragarph="  My name is p.sri durga devi.  who is trying to learn  python bacis.  as a fresher. which is usefull to me to find a job.  " 
# #     paragarph=paragarph.strip()
# #     text=paragarph.split(".")
# #     print(text)
# #     print(len(paragarph))
# # ass1() 

# # def ass2():
# #     my_list=[]
# #     name=input("enter your first name: ")
# #     sur=input("enter your sur name: ")
# #     my_list.append(name)
# #     my_list.append(sur)
# #     print("_".join(my_list))
# #     print(my_list)
# # ass2()


# # def ass3():
# #       text=" i am to lazy to do my daily home work and also boring to attend the daily class"
# #       print(text.replace("lazy","hardworking").replace("boring","active"))
# # ass3()

# s="  Hello "
# print(s.strip())

# text=" i love java "
# print(text.replace("love","hate"))
# print(text.strip())

# # data="apple,banana,mango"
# # text="i am ahuman + who is + trying + to + learn + python"
# # print(text.strip("+"))
# # print(data.split("+"))


# data = "apple,banana,mango"
# text = "i am a human + who is + trying + to + learn + python"
# life = print(text.strip("+"))  # Output: ['i am a human ', ' who is ', ' trying ', ' to ', ' learn ', ' python']
# print(data.split("+"))  # Output: ['apple', 'banana', 'mango']

# fruits=['apple','banana','mango']
# print(",".join(fruits))

# def clean_text(blog):
#       blog=blog.strip("/")
#       blog=blog.replace("teh","the")
#       words=blog.split(".")
#       cleaned=" ".join(words)
#       return cleaned
# blog=input("enter your blog post: ")
# print("cleaned blog:",clean_text(blog))
# clean_text(blog)


#  spells=["fireball","tceblast","dark_veil"]
#  cleaned_spells=[]
#  for spell in spells:
#       spell=spell.strip().replace("_"," ").title()
#       cleaned_spells.append(spell)
# print("your spellbook: ")
# for s in cleaned_spells:
#       print("_",s)

# spells = ["  FireBall ", "ICE blast", "dark_VEIL"]

# # Clean spell names
# cleaned_spells = []
# for spell in spells:
#     spell = spell.strip().replace("_", " ").title()
#     cleaned_spells.append(spell)

# print("Your Spellbook:")
# for s in cleaned_spells:
#     print("_", s)

def day():
    names=input("enter their names: ")
    for i in range(0,50):
        print("\U0001f600 \u2764\ufe0f happy aniversary  \u2764\ufe0f")
day()


