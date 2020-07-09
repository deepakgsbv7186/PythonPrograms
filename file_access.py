# import os,sys
# if os.path.isfile("test.txt"):
#     print("exits")
#     f = open('test.txt')
#     # f.write("In test file")
#     print(f.read())
#     f.close()


with open("test.txt") as f:
    print(f.readlines())
