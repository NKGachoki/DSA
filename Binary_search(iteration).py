# A simple program to create, sort and search a list of integers

# Creating and sorting list

l = list()
integers = int(input("Please enter the no. of integers in the list: "))
print(f"Please enter {integers} integers: ")
for i in range(integers):
    l.append(int(input()))
l.sort()
print("List created and sorted.")

# Binary search algorithm to find element in list via iteration
s = int(input("Enter integer to be searched: "))
first_index = 0
last_index = len(l) - 1
mid_index= None
while first_index <= last_index:
    mid_index = (first_index + last_index) // 2
    if l[mid_index] == s:
        print(f"\"{s}\" found at index position \"{mid_index}\"")
        break
    elif l[mid_index] > s:
        last_index = mid_index - 1
    else:
        first_index = mid_index + 1
else:
    print(f"\"{s}\" not found.")