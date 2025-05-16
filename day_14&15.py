# with open("day_1.py","r") as file:
#     print(file.read())
 
# def journal():
#     with open("journal.txt",'a') as file:
#         line=input("enter the today journal: ")
#         file.write(line + "\n")
#     with open("journal.txt",'r')as file:
#         print(file.read()) 
# def overwrite():
#     with open("journal.text",'w')as file:
#         line2=input("enter the journal: ")
#         file.write(line2 + "\n")
#     with open("journal.txt",'r')as file:
#         print(file.read()) 
# overwrite()   
# journal()

# import json
# data = {"name": "Hero", "level": 5, "score": 300}
# data = {"name": "villan", "level": 9, "score": 900}
# with open("player.json", "w") as file:
#     json.dump(data, file)

# with open("player.json", "r") as file:
#     loaded_data = json.load(file)
#     print(loaded_data["name"],[loaded_data["level"]], loaded_data["score"])


# import csv

# try:
#     # Try to open the file in read mode
#     with open("stats.csv", newline='') as file:
#         reader = csv.reader(file)
#         print("📄 Reading existing file:")
#         for row in reader:
#             print(row)

# except FileNotFoundError:
#     # If the file doesn't exist, create it
#     print("⚠️ File not found. Creating 'stats.csv'...")
#     with open("stats.csv", "w", newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Name", "Score"])
# #         writer.writerow(["name","score"])


# def simple_dairy():
#     new_entry=input("enter your today journal: ")
#     with open("dairy.txt",'w') as file:
#         print(file.write(new_entry))
#     with open("dairy.txt",'a') as file:
#         line=input("add to today journal:")
#         print(file.write( "\t" + line))
#     with open("dairy.txt",'r') as file:
#         print(file.read())
    
# simple_dairy()



text=input("enter data in journal.txt: ")
with open("journal.txt",'w') as file:
    print(file.write(text))
try:
    with open("journal1.txt",'r') as file:
        lines=file.readlines()
        num_lines=len(lines)
        num_words = sum(len(line.split()) for line in lines) 
        print(lines)
        print("number of lines ",num_lines)
        print("number of words",num_words)
except FileNotFoundError:
    print("file not found creat a new file")


