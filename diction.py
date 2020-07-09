# di = {"appy":"burger",
# "harry":"fast food","gabby":{"a":"pasta","b":"maggie"}}
# # di["ankit"] = "pizza"
# # print(di.items())
# # del di["ankit"]
# di.update({"leena":"coffee"})

# print(di.keys())
# print()
dj = {}
for i in range(4):
    x = input('Enter key: ')
    y = input('Enter value: ')
    dj.update({x:y})
print(dj)
z = input('Search key: ')
print(dj[z])