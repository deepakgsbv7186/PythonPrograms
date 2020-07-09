# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
def calc():
    x = int(input("Enter num1: "))
    y = int(input("Enter num2: "))
    operator = input("Operation: ")
    print("Result:",end=" ")
    if operator == '+':
        if (x == 56) and (y == 9):
            print(77)
        else:
            print(x+y) 
    elif operator == '-':
        print(x-y) 
    elif operator == '*':
        if x == 45 and y == 3:
            print(555)
        else:
            print(x*y) 
    elif operator == '/':
        if x == 56 and y == 6:
            print(4)
        else:
            print(x/y) 
    else:
        print("Happy To Help")

# the main program starts here
print("Welcome To Faulty Calculator")
print("[+ add]","[- sub]","[* mul]","[/ div]")
while (True):
    calc()
    if((input("Do you want to continue calculating?(Y/N)\n")).capitalize()=='Y'):
        print("Some more calculations...")
        continue
    else:
        print("Thank You for using the Calculator")
        break


