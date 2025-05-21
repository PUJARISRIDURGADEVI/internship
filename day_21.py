# add=lambda x,y:x+y
# print(add(3,4))


# is_even=lambda x:x%2==0
# print((is_even(4)))

# sub=lambda a,b,c:a-b-c
# print(sub(2,3,4))

my_list=[2,4,6,8]
square=list( map(lambda x:x**2, my_list))
print(square)

# num=[5, 12, 17, 18, 24, 33]
# even=list(filter(lambda x:x%2==0,num))
# print(even)

# from functools import reduce
# num=[1, 2, 3, 4, 5]
# multiply=reduce(lambda x,y:x*y,num)
# print(multiply)


# usernames= [" Alice ", " Bob ", " Charlie ", " Dana "]
# remove_whitespaces=list(map(lambda x:x.strip(),usernames))
# print(remove_whitespaces)

# list_of_words=["tree", "apple", "sun", "python", "code"]
# filter_the_words=list(filter(lambda x:len(x)>=5,list_of_words))
# print(filter_the_words)

# factor= [10, 20, 30]
# spell_power=list(map(lambda x:x*1.5,factor))
# # print(spell_power)

# from functools import reduce
# scores= [250, 180, 320, 150]
# total=reduce(lambda x,y:x+y,scores)
# print(total)

# given_list=[-1,-2,3,4,5,6,7,8,-9,-10]
# postive_numbers=list(filter(lambda x:x>0,given_list))
# negative_numbers=list(filter(lambda x:x<0,given_list))
# odd_numbers=list(filter(lambda x:x%2!=0,given_list))
# print(postive_numbers)
# print(negative_numbers)
# print(odd_numbers)


# text="hello world from python"
# text2=text.split()
# capitalize_text=list(map(lambda x:x.capitalize(),text2))
# print(capitalize_text)
 
from functools import reduce
input= ["Alice", "Bob", "Charlie"]
single_string=reduce(lambda x,y:" & ".join([x,y]),input)
print(single_string)