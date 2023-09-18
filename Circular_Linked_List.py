class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

# Method to insert node at the beginning of the list
    def insert_beginning(self, data=None):
        try:
            nb = Node(data)
            if data is None:
                print("Error at method: insert_beginning()! Missing argument! Please enter value of node.")
            elif self.head is None:
                nb.next = nb
                self.head = nb
            else:
                nb.next = self.head
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = nb
                self.head = nb
        except Exception as e:
            print(e)

# Method to delete node at the beginning of the list
    def delete_beginning(self):
        try:
            if self.head is None:
                print("Error! Cannot delete node at beginning as list is already empty.")
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = temp.next
        except Exception as e:
            print(e)
        
# Method to insert node at the end of the list
    def insert_end(self, data=None):
        try:
            ne = Node(data)
            if data is None:
                print("Error at method: insert_end()! Missing argument! Please enter value of node.")
            elif self.head is None:
                ne.next = ne
                self.head = ne
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = ne
                ne.next = self.head
        except Exception as e:
            print(e)

# Method to delete node at the end of the list
    def delete_end(self):
        try:
            if self.head is None:
                    print("Error! Cannot delete node at end as list is already empty.")
            else: 
                temp = self.head.next
                prev = self.head
                while temp.next != self.head:
                    temp = temp.next
                    prev = prev.next
                prev.next = self.head
                temp.next = None
        except Exception as e:
            print(e)

# Method to insert node at any position in the list
    def insert_anyposition(self, data=None, index_pos=None):
        try:
            ni = Node(data)
            if data is None and index_pos is None:
                print("Error at method: insert_anyposition()! Missing 2 arguments! Please enter value of node and desired index position of node")
            elif data is None:
                print("Error at method: insert_anyposition()! 1st argument missing! Please enter value of node.")
            elif index_pos is None:
                print("Error at method: insert_anyposition()! 2nd argument missing! Please enter desired index position of node.")
            elif index_pos > 0 and self.head is None:
                print("Error at method: insert_anyposition()! Can't insert node at index position as list is empty. Please insert node at index 0.")
            elif index_pos < 0:
                print("Error at method: insert_anyposition()! Numerical position of node can't be less than 1.")
            elif index_pos == 0:
                self.insert_beginning(data)
            else:
                temp = self.head
                for i in range(index_pos - 1):
                    temp = temp.next
                ni.next = temp.next
                temp.next = ni
        except Exception as e:
            print(e)

# Method to delete node at any position in the list
    def delete_anyposition(self, index_pos=None):
        try:   
            if index_pos is None:
                print("Error at method: delete_anyposition()! Missing argument! Please specify index position of node.")
            elif self.head is None:
                print("Error at method: delete_anyposition()! Cannot delete node at specified index position as list is already empty.")
            elif index_pos < 0:
                print("Error at method: delete_anyposition()! Index position of node to be deleted can't be less than 0.")
            elif index_pos == 0:
                self.delete_beginning()
            else:
                temp = self.head.next
                prev = self.head
                for i in range(index_pos - 1):
                    temp = temp.next
                    prev = prev.next
                prev.next = temp.next
                temp.next = None
        except Exception as e:
            print(e)

# Method to delete entire list
    def deletelist(self):
        try:
            temp = self.head
            temp.next = None
            self.head = None
        except Exception as e:
            print(e)

# Method to count and display the no. of nodes in the list
    def nodecount(self):
        try:
            if self.head is None:
                count = 0
            else:
                temp = self.head
                count = 1
                while temp.next != self.head :
                    temp = temp.next
                    count = count + 1
            print(f"Node count: {count}")
        except Exception as e:
            print(e)

# Method to search for data in the list
    def search(self, data=None):
        try:
            count = 1
            temp = self.head
            if self.head is None:
                print("Error at method: search()! Cannot search as list is empty.")
            elif data == None:
                print("Error at method: search()! Missing argument! Please enter data to be searched.")
            else:
                while temp.next != self.head:
                    if data == temp.data:
                        print(f"{data} found at node {count}")
                        break
                    else: 
                        temp = temp.next
                        count = count + 1
                        if temp.next == self.head and data != temp.data:
                            print("Error at method: search()! Could not find node.")
        except Exception as e:
            print(e)

# Method to display the list in stdout
    def display(self):
        try:
            if self.head is None:
                print("The list is empty.")
            else:
                temp = self.head
                print(temp.data, end=" ")
                while temp.next != self.head:
                    temp = temp.next
                    print(temp.data, end=" ")
                print(self.head.data) # Prints out the value of the 1st node which is pointed to by the last node thus illustrating the 'circuler' structure of the list.
        except Exception as e:
            print(e)







