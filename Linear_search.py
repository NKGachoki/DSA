# A simple program to illustrate the use of a linear search algorithm in a list

# Creating and populating list.
simple_list = list()
element = int(input("Please enter the no. of elements to be put in the list: "))
print(f"Please enter {element} elements")
for i in range(element):
    value = input()
    simple_list.append(value)
print("List populated.")

# Linear search algorithm to find element in list
element = input("Enter element to be searched:")
if element in simple_list:
    print(f"\"{element}\" found at index \"{simple_list.index(element)}\"")
else:
    print("Element not found")