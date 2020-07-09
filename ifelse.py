list_items = [1,5,34,7]
find_in_list = int(input("Search for: "))

# print(type(find_in_list))

if find_in_list in list_items:
    print(list_items)
else:
    print("not found")