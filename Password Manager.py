loop1 = 0
Names = []
items = []
passed = 0
welcome = input("Welcome to your Password Manager, Do you have an account? (y or n)")


####login#####
if welcome == "y":
    user = input("Username:")
    pas = input("Password:")
    ui = (user , pas)
    file2 = open("DataBase.txt","r")
    login = file2.readlines()
    if ui == login:
        print("YOU DID IT!!!")
    else:
        print("WHOMP WHOMP")

####login#####

####register#####
if welcome == "n":
    username = input("username: ")
    password = input("password: ")
    UI = (username, password)
    fileToWriteTo = open("DataBase.txt", "w")
    fileToWriteTo.write(str(UI))
    fileToWriteTo.close()
    
####register#####

###appending to database######

#!!!!!!!!!!THIS PART NEEDS WORK!!!!!!!!!!!#
    
#!!!!!!!!!!THIS PART NEEDS WORK!!!!!!!!!!!#
###appending to database#####
'''
class Student:
     
     #Constructor
     def __init__(self,Name,Username,Password):
          self.FullName = Name
          self.UsernameInput = Username
          self.passwordinput = Password
          self.courses=[]

     #toString          
     def __str__(self):
          out=f"{self.UsernameInput},{self.FullName},{self.passwordinput}\n"
          #for localVariable in list
          for c in self.courses:
               #concat to the out variable
               out+=f"\t{c}\n"
          return out
     
     #getters
     def getFirstName(self):
          return self.FullName
     
     def getLastName(self):
          return self.UsernameInput
      
     def getLastName(self):
          return self.passwordinput
     
     #setter
     def addCourse(self,newCourse):
          self.courses.append(newCourse)
    
'''