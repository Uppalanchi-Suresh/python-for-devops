random_list = (1, 2, 3, "Hello", 3.14)
random_list1 = [1, 2, 3, "Hello", 3.14]

if random_list1 != random_list:
    random_list1.append("World")
    print("The list and tuple are not the same, Adding a new element to the list")
else:
    print("Both the list and tuple are the same, so we cannot add 'World' to the tuple.")    

print("A new word, 'World' has been added to the list, but not to the tuple.")

print(random_list1)