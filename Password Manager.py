loop1 = 0
Names = []
items = []
passed = 0

welcome = input("Welcome to your Password Manager, Do you have an account? (y or n)")
    
    ####loop####
    #####loop####
    
####login#####
if welcome == "y":
    user = input("Username:")
    pas = input("Password:")
    file2 = open("DataBase.txt","r")
    file3 = file2.readlines()
    print(file3)
    for i in file3:
        if user and pas in file3:
            passed += 1
            
####login#####

####register#####
if welcome == "n":
    newname = input("Type in your Name:")
    newuser = input("Type in a username:")
    newpas = input("Type in a password:")
    
####register#####

###appending to database######

#!!!!!!!!!!THIS PART NEEDS WORK!!!!!!!!!!!#
    firstspace = "\n"
    secondspace = "\n"
    items.append(newname)
    items.append(firstspace)
    items.append(newuser)
    items.append(secondspace)
    items.append(newpas)
    file = open('DataBase.txt', "w")
    file.writelines(items)
    file.close()
#!!!!!!!!!!THIS PART NEEDS WORK!!!!!!!!!!!#
###appending to database#####

    
