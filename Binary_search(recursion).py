# A simple program to create, sort and search a list of integers

# Binary search algorithm to find element in list via recursion
def binary_search(l, first_index, last_index, mid_index, s):
    if first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if l[mid_index] == s:
            print(f"\"{s}\" found at index position \"{mid_index}\"")
        elif l[mid_index] > s:
            binary_search(l, first_index, mid_index - 1, mid_index, s)
        else:
            binary_search(l, mid_index + 1, last_index, mid_index, s)
    else:
        print(f"\"{s}\" not found in list.")

# Creating and sorting list
l = list()
elements = int(input("Please enter no. of integers in list: "))
print(f"Enter {elements} integers: ")
for i in range(elements):
    l.append(int(input()))
l.sort()
print("List created and sorted.")
s = int(input("Please enter integer to be searched: "))

first_index = 0
last_index = len(l) - 1
mid_index = None
binary_search(l, first_index, last_index, mid_index, s)
