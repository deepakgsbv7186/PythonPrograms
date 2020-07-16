# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *
# print("Pattern printing")
# num = int(input("Enter num how many rows you want : "))
# print("Enter 1 or 0")
# bool_val = input("1 for True value or 0 for False : ")
# if bool_val=="1":
#     for i in range(0,num+1):
#         print("*"*i)
#
# if bool_val=="0":
#     for i in range(num,0,-1):
#         print("*"* i)


rows = int(input("Enter the row to print: "))
print("(1 -> Up 0 -> Down) Pyramid")
ward = bool(int(input("Choose: ")))

def star(rows, ward):
    if ward == True:
        c = 1
        while c <= rows:
            print(c * "*")
            c +=1
    else:
        while rows > 0:
            print(rows * "*")
            rows -= 1

star(rows, ward)
  
