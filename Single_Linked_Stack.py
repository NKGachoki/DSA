# A program to create a stack via a single linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

# Method to push data to stack
    def push(self, data):
        try:
            nb = Node(data) 
            nb.next = self.head
            self.head = nb
        except Exception as e:
            print(e)

# Method to pop data from stack
    def pop(self):
        try:
            if self.head is None:
                print("Error @ method: pop()! Stack is already empty.")
            else:
                temp = self.head
                self.head = temp.next
                temp = None
        except Exception as e:
            print(e)

# Method to count the no. of nodes in the stack
    def node_count(self):
        try:
            if self.head is None:
                count = 0
                print(f"Node count: {count}")
            else:
                temp = self.head
                count = 1
                while temp.next is not None:
                    temp = temp.next
                    count = count + 1
                print(f"Node count: {count}")
        except Exception as e:
            print(e)

# Method to display the stack and its contents to stdout
    def display(self):
        try:
            if self.head is None:
                print("Error @ method: display()! Stack is already empty.")
            else:
                temp = self.head
                while temp is not None:
                    print(temp.data)
                    temp = temp.next
        except Exception as e:
            print(e)

# Method to pop all content from the stack
    def pop_stack(self):
        try:
            if self.head is None:
                print("Error @ method: pop_stack()! Stack is already empty.")
            else:
                temp = self.head
                temp.next = None
                self.head = None
        except Exception as e:
            print(e)

# Example of applying the above code to push and pop data into a single linked stack.

stack = Stack()

print("After pushing data to stack...")
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.display()
stack.node_count()

print("\nAfter popping some data from the stack...")
stack.pop()
stack.pop()
stack.display()
stack.node_count()

print("\nAfter popping all the data from the stack...")
stack.pop_stack()
stack.node_count()


       