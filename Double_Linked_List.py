class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

# Method to insert node at the beginning of the list
    def insert_beginning(self, data=None):
        try:
            nb = Node(data)
            if data is None:
                print("Error at method: insert_beginning()! Missing argument! Please enter value of node.")
            elif self.head is None:
                nb.next = self.head
                nb.prev = None
                self.head = nb
            else:
                temp = self.head
                temp.prev = nb
                nb.next = temp
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
                self.head = temp.next
                temp.next.prev = None
                temp.next = None
        except Exception as e:
            print(e)

# Method to insert node at the end of the list
    def insert_end(self, data=None):
        try:
            ne = Node(data)
            if data is None:
                print("Error at method: insert_end()! Missing argument! Please enter value of node.")
            elif self.head is None:
                ne.next = self.head
                self.head = ne
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = ne
                ne.prev = temp
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
                while temp.next is not None:
                    temp = temp.next
                    prev = prev.next
                temp.prev = None
                prev.next = None
        except Exception as e:
            print(e)

# Method to insert node at any position in the list
    def insert_anyposition(self, data=None, index_pos=None):
        try:
            np = Node(data)
            if data is None and index_pos is None:
                print("Error at method: insert_anyposition()! Missing 2 arguments! Please enter value of node and desired index position of node")
            elif data is None:
                print("Error at method: insert_anyposition()! 1st argument missing! Please enter value of node.")
            elif index_pos is None:
                print("Error at method: insert_anyposition()! 2nd argument missing! Please enter desired index position of node.")
            elif index_pos > 0 and self.head is None:
                print("Error at method: insert_anyposition()! Can't insert node at index position as list is empty. Please insert node at index 0.")
            elif index_pos < 0:
                print("Error at method: insert_anyposition()! Index position of node can't be less than 0")
            elif index_pos == 0:
                self.insert_beginning(data)
            else:
                temp = self.head
                for i in range(index_pos - 1):
                    temp = temp.next
                np.prev = temp
                np.next = temp.next
                temp.next.prev = np
                temp.next = np
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
                print("Error at method: delete_anyposition()! Index position of node to be deleted can't be less than 0")
            elif index_pos == 0:
                self.delete_beginning()
            else:
                temp = self.head.next
                prev = self.head
                for i in range(index_pos - 1):
                    temp = temp.next
                    prev = prev.next
                prev.next = temp.next
                temp.next.prev = prev
                temp.next = None
                temp.prev = None
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
                while temp.next is not None :
                    temp = temp.next
                    count = count + 1
            print(f"node count: {count}")
        except Exception as e:
            print(e)

# Method to search for data in the list
    def search(self, data=None):
        try:
            count = 1
            temp = self.head
            if self.head is None:
                print("\nError at method: search()! Cannot search as list is empty.")
            elif data == None:
                print("\nError at method: search()! Missing argument! Please enter data to be searched.")
            else:
                while temp.next is not None:
                    if data == temp.data:
                        print(f"\n{data} found at node {count}")
                        break
                    else: 
                        temp = temp.next
                        count = count + 1
                        if temp.next is None and data != temp.data:
                            print("\nError at method: search()! Could not find node.")
        except Exception as e:
            print(e)

# Method to display the list in stdout
    def display(self):
        try:
            if self.head is None:
                print("The list is empty.")
            else:
                temp = self.head
                while temp is not None:
                    print(temp.data, end=" ")
                    temp = temp.next
        except Exception as e:
            print(e)


