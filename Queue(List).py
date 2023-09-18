# Simple program to create and display a queue via a list

# Function to enqueue values to the queue 
def enqueue():
    try:
        print("Enqueue option selected...")
        value = input("Please enter value: ")
        queue.append(value)
    except Exception as e:
        print(e)

# Function to dequeue values from the queue
def dequeue():
    try:
        print("Dequeue option selected...")
        print(f"\"{queue[0]}\" has been deqeueud.")
        del queue[0]
    except Exception as e:
        print(e)

# Function to display the queue and its contents to stdout
def display():
    try:
        print("Display option selected...")
        if len(queue) == 0:
            print("Error! Queue is empty.")
        else:
            print("The queue is as follows:")
            for i in queue:
                print(i)
    except Exception as e:
        print(e)

# Function to delete all the contents of the queue
def delete_queue():
    try:
        if len(queue) == 0:
            print("Error! Queue is already empty.")
        else:
            response = input("Are you sure you'd like to delete the contents of the entire queue? Enter \"yes\" or \"no\"")
            if response == "yes":
                print("Queue content deleted. Queue is now empty.")
                queue.clear()
            elif response == "no":
                return
            elif response != "yes" and response != "no":
                print("Invalid answer given. Please try again.")
                delete_queue()
    except Exception as e:
        print(e)
        
queue = list()
try: 
    while True:
        print("Please enter any of the following options:\n1 - To enqueue (insert) data into the queue.\n2 - To dequeue (delete) data from the queue.\n3 - To display the contents of the queue.\n4 - To delete the entire queue.\nexit - To exit the program ")
        option = input("Enter option:")
        if option == "1":
            enqueue()
        elif option == "2":
            dequeue()
        elif option == "3":
            display()
        elif option == "4":
            delete_queue()
        elif option == "exit":
            print("Program exited.")
            break
except Exception as e:
    print(e)