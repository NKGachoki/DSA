# Simple program to create and display a stack via a list

# Function to push values to the stack
def push():
    try:
        print("Push Option selected...")
        value = input("Please enter value:")
        if len(stack) == 0:
            stack.append(value)
        else:
            stack.insert(0, value)
    except Exception as e:
        print(e)

# Function to pop values from the stack
def pop():
    try:
        print("Pop Option selected...")
        if len(stack) == 0:
            print("Error! Stack is empty.")
        else:
            print(f"\"{stack[0]}\" has been popped from the stack")
            del stack[0]
    except Exception as e:
        print(e)

# Function to pop all the contents of the stack
def pop_stack():
    if len(stack) == 0:
        print("Error! Stack is already empty.")
    else:
        response = input("Are you sure you'd like to delete the contents of the entire stack? Enter \"yes\" or \"no\" ")
        if response == "yes":
            print("Stack content deleted. Stack is now empty.")
            stack.clear()
        elif response == "no":
            return
        elif response != "yes" and response != "no":
            print("Wrong answer given. Please try again.")
            pop_stack()

# Function to display the stack and its contents to stdout
def display():
    try:
        print("Display Option selected...")      
        if len(stack) == 0:
            print("Error! Stack is empty.")
        else:
            print("The stack is as follows:")
            for i in stack:
                print(i)
    except Exception as e:
        print(e)

stack = list()
try: 
    while True:
        print("Please enter any of the following options:\n1 - To push (insert) data into the stack.\n2 - To pop (delete) data from the stack.\n3 - To display the contents of the stack.\n4 - To delete all contents of the stack.\nexit - To exit the program ")
        option = input("Enter option:")
        if option == "1":
            push()
        elif option == "2":
            pop()
        elif option == "3":
            display()
        elif option == "4":
            pop_stack()
        elif option == "exit":
            print("Program exited.")
            break
except Exception as e:
    print(e)
