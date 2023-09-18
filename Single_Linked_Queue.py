# A program to create a queue via a single linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

# Method to enqueue data 
    def enqueue(self, data):
        try:
            ne = Node(data)
            temp = self.head
            if self.head is None:
                ne.next = self.head
                self.head = ne
            else:
                while temp.next is not None:
                    temp = temp.next
                ne.next = temp.next
                temp.next = ne
        except Exception as e:
            print(e)

# Method to dequeue data
    def dequeue(self):
        try:
            if self.head is None:
                print("Error @ method: dequeue()! The queue is already empty.")
            else:
                temp = self.head
                self.head = temp.next
                temp.next = None
        except Exception as e:
            print(e)

# Method to count no. of nodes in queue
    def node_count(self):
        try:
            if self.head is None:
                count = 0
                print(f"Node count: {count}")
            else:
                count = 1
                temp = self.head
                while temp.next is not None:
                    count = count + 1
                    temp = temp.next
                print(f"Node count: {count}")
        except Exception as e:
            print(e)
        
 # Method to display the queue and its contents to stdout       
    def display(self):
        try:
            if self.head is None:
                print("Error @ method: display()! The queue is already empty.")
            else:
                temp = self.head
                while temp is not None:
                    print(temp.data)
                    temp = temp.next
        except Exception as e:
            print(e)

# Method to dequeue the entire queue
    def dequeue_queue(self):
        try:
            if self.head is None:
                print("Error @ method: dequeue_queue()! The queue is already empty.")
            else:
                temp = self.head
                temp.next = None
                self.head = None
        except Exception as e:
            print(e)


