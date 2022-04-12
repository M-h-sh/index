from itertools import count
import pickle as pickle

users = []

def serialize(filename,target):
    with open(filename, 'wb') as output:
     pickle.dump(target, output, pickle.HIGHEST_PROTOCOL)

def deserialize(filename):
    with open(filename, 'rb') as input:
     return pickle.load(input)

    #users = deserialize("filename.txt")

for i in count(0):

         print("1 - Add a user")
         print("2 - Delete a user")
         print("3 - Update a user")
         print("4 - List users")
         print("5 - Exit")

         command = input(":")
         if(command == "1"):
                      print("You have decided to add a user")
                      user = {}
                      name = input("Enter your name: ")
                      user["name"] = name
                      surname = input("Enter your surname: ")
                      user["surname"] = surname
                      email = input("Enter your email address: ")
                      user["email"] = email
                      date_of_birth = input("Input your date of birth DD/MM/YYYY: ")
                      user["date_of_birth"] = date_of_birth
                      age = 2021 - int(date_of_birth.split('/')[2])
                      user["age"] = age
                      users.append(user)
                      print("Hello, " + name + " " + surname + " your details have been saved to the database.")
                      serialize("filename.txt",users)

         elif (command == "2"): 
                      print("You have decided to delete a user.")  
                      email = input("Enter your email address: ")      
                      for arr in users:
                              if(arr.get('email') == email and arr['email'] == email):
                                        users.remove(arr)
                
         elif(command == "3"):
                       print("You have decided to Update a users")
                       email = input("Enter your email address: ")
                       users.append(email)
                       print(users)

         elif(command == "4"):
                       print("You have decided to list users")
                       name = input("Please enter your name: ")
                       for arr in users:
                               if(arr.get('name') == name and arr['name'] == name):
                                          print(arr)

         elif(command == "5"):
                       print("Exit.")
                       break;

         else:
             print("you have entered an invalid option.")
