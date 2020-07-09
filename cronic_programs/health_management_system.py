# Health Management System
# 3 Clients Vinay, Sanjeet and Raman
# Handling with 3 files, one for each client
# Take logs for diet of clients (input)
# [Date, Time] Food_Name (output)
def getDate():
    import datetime
    return datetime.datetime.now()

cl_name = {"1":"vinay_diet.txt", "2":"sanjeet_diet.txt", "3":"raman_diet.txt"}

def PreferClient():
    print("\n  Welcome To Diet Log3 System")
    print("*"*30)
    print("1 -> Vinay  2 -> Sanjeet  3 -> Raman")
    client = input('Choose Client: ')
    # print(cl_name[client])
    diet_logs(client)
    print("")
    print("*"*30)

def switch_client():
    pass
    

def diet_logs(client):
    f = open(cl_name[client], "a+")
    option = input("Press 'r' to Display || 'w' to Add Log: ")
    print("\nClient File: ",cl_name[client])
    if(option == 'w'):
        print("Please enter only one at time...")
        dt = str(getDate())
        item_name = input("Enter Diet: ")
        f.write("\n" + "[ "+ dt + " ]" + "   " + item_name)
    else:
        f.seek(0)
        print(f.read())
    f.close()


while (True):
    PreferClient()
    if((input("Do you want to continue?(Y/N)\n")).capitalize()=='Y'):
        print("Add more...")
        continue
    else:
        print("We keep save your diet logs...")
        break
