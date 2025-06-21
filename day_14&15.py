with open("day_1.py","r") as file:
    print(file.read())
 
def journal():
    with open("journal.txt",'a') as file:
        line=input("enter the today journal: ")
        file.write(line + "\n")
    with open("journal.txt",'r')as file:
        print(file.read()) 
def overwrite():
    with open("journal.text",'w')as file:
        line2=input("enter the journal: ")
        file.write(line2 + "\n")
    with open("journal.txt",'r')as file:
        print(file.read()) 
overwrite()   
journal()

import json
data = {"name": "Hero", "level": 5, "score": 300}
data = {"name": "villan", "level": 9, "score": 900}
with open("player.json", "w") as file:
    json.dump(data, file)

with open("player.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["name"],[loaded_data["level"]], loaded_data["score"])


import csv

try:
    # Try to open the file in read mode
    with open("stats.csv", newline='') as file:
        reader = csv.reader(file)
        print("📄 Reading existing file:")
        for row in reader:
            print(row)

except FileNotFoundError:
    # If the file doesn't exist, create it
    print("⚠️ File not found. Creating 'stats.csv'...")
    with open("stats.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Score"])
        writer.writerow(["name","score"])


def simple_dairy():
    new_entry=input("enter your today journal: ")
    with open("dairy.txt",'w') as file:
        print(file.write(new_entry))
    with open("dairy.txt",'a') as file:
        line=input("add to today journal:")
        print(file.write( "\t" + line))
    with open("dairy.txt",'r') as file:
        print(file.read())
    
simple_dairy()



text=input("enter data in journal.txt: ")
with open("journal.txt",'w') as file:
    print(file.write(text))
try:
    with open("journal.txt",'r') as file:
        lines=file.readlines()
        num_lines=len(lines)
        num_words = sum(len(line.split()) for line in lines) 
        print(lines)
        print("number of lines ",num_lines)
        print("number of words",num_words)
except FileNotFoundError:
    print("file not found creat a new file")


def keyword_search():
    text=input("enter the text: ")
    with open("notes.txt",'w') as file:
        print(file.write(text))
    with open("notes.txt",'r') as file:
        print(file.read())
    try:
        search_word=input("enter word to search: ")
        if search_word in text:
            print(f" search word in text {search_word}")
        else:
            print("search word not in text")
    except FileNotFoundError:
        print("file is not found to search the word")
keyword_search()  


name=input("enter the name: ")
score=input("enter the score: ")
with open("result.txt","a") as file:
    print(file.write(name))
    print(file.write(score))
with open("result.txt",'r') as file:
     print("\n show all entries")
    print(file.read()  )

import  csv
def student_grade():
    name=input("enter name of the student: ")
    marks=input("enter the marks of the student: ")
    try:
        with open("grade.csv",'w',newline='')as file:
            writer=csv.writer(file)
            writer.writerow(["name",'marks'])
            writer.writerow([name,marks])
        with open("grade.csv",'r',newline='') as file:
            print("student grade")
            reader=csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("file not found create a new file")

student_grade()


import csv
def  inventory():
    total=0
    with open("inventory.csv","w",newline='') as file:
        writer=csv.writer(file)
        for i in range(2):
            product=input("enter the product name: ")
            price=float(input("enter their product price: "))
            writer.writerow([product,price])
    with open("inventory.csv","r",newline='') as file:
        reader=csv.reader(file)
        for row in reader:
            if len(row) == 2:
                try:
                    total += float(row[1])
                except ValueError:
                    print(f"Invalid price found: {row[1]}")

    print(f"Total value of all products: {total:f}")

inventory()


import json
monstar=[{"name":"Shadow Maw","type":"Dark","power":"Absorbs light and emits a chilling aura"},
{"name":"Pyrofang","type":"Fire","power":"Unleashes fire blasts and molten claws"},
{"name":"Thunderbeast","type":"Electric","power":"Summons storms and releases lightning strikes"}]
with open("monstar.json","w") as file:
    json.dump(monstar,file)
search_name=input("enter the monstar name to search: ")
with open("monstar.json","r")as file:
        loaded_data=json.load(file)
for monstar in loaded_data:
    if search_name==monstar['name']:
        print(f"name:{monstar['name']}\n type:{monstar['type']}\n power:{monstar['power']}")
        break
else:
    print("monstar name is not in the file")


import csv
def contact_manager():
    contact_list=[]
    with open("contact.csv",'w',newline='') as file:
        writer=csv.writer(file)
        for row in range(2):
            name=input("enter the name :" )
            ph_no=input("enter the ph number: ")
            email=input("enter the email id: ")
            writer.writerow([name,ph_no,email])
    with open("contact.csv",'r',newline='') as file:
        reader=csv.reader(file)
        print("veiw all the contacts: ")
        for row in reader:
            print(row)
            contact_list.append(row)
    search_name=input("enter name to search: ")
    for contact in contact_list:
        if  contact[0] == search_name:
            print(f"contact name: {contact}")
            break
        else:
            print("not found")
    add_contact=input("add the contact: ")
    if add_contact in contact_list:
        print("name is already exsist:")
    else:
        ph_no=input("enter the ph number: ")
        email=input("enter the email id: ") 
contact_manager()
