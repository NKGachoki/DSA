class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    #Method to insert node to binary tree
    def insert(self, value):
        try:
            self.value = value
            self._insert(self.root, value)
        except Exception as e:
            print(e)

    def _insert(self, parent, value):
        try:
            if self.root is None:
                self.root = Node(value)
            else: 
                if value < parent.value:
                    if parent.left is None:
                        parent.left = Node(value)
                    else:
                        self._insert(parent.left, value)
                elif value > parent.value:
                    if parent.right is None:
                        parent.right = Node(value)
                    else:
                        self._insert(parent.right, value)
                elif value == parent.value:
                    print(f"\"{value}\" already entered in binary tree.")
        except Exception as e:
            print(e)

    # Method to traverse and print out binary tree in preorder, inorder or postorder traversal
    def print_tree(self, option=None):
        try:
            option = input("Inorder to traverse the binary tree please enter any of the following options:\n1 - for Preorder-traversal\n2 - for Inorder-traversal\n3 - for Postorder-Traversal\noption selected:  ")
            if option == "1":
                print("Preorder-traversal selected...")
                print(self.Preorder_Traversal(self.root, ""))
            elif option == "2":
                print("Inorder-traversal selected...")
                print(self.Inorder_Traversal(self.root, ""))
            elif option == "3":
                print("Postorder-traversal selected...")
                print(self.Postorder_Traversal(self.root, ""))
        except Exception as e:
            print(e)

    def Preorder_Traversal(self, start, tree_values):
        try:
            if start is not None:
                tree_values += (str(start.value) + " ")
                tree_values = self.Preorder_Traversal(start.left, tree_values)
                tree_values = self.Preorder_Traversal(start.right, tree_values)
            return tree_values
        except Exception as e:
            print(e)
    
    def Inorder_Traversal(self, start, tree_values):
        try: 
            if start is not None:    
                tree_values = self.Inorder_Traversal(start.left, tree_values)
                tree_values += (str(start.value) + " ")
                tree_values = self.Inorder_Traversal(start.right, tree_values)
            return tree_values
        except Exception as e:
            print(e)
    
    def Postorder_Traversal(self, start, tree_values):
        try:
            if start is not None:
                tree_values = self.Postorder_Traversal(start.left, tree_values)
                tree_values = self.Postorder_Traversal(start.right, tree_values)
                tree_values += (str(start.value) + " ")
            return tree_values
        except Exception as e:
            print(e)
    
    # Method to search for value in binary tree
    def search(self, value):
        try:
            self.value = value
            if self.root is None:
                print("Error @ method: search()! Binary tree is empty.")
            else:
                self._search(self.root, value)
        except Exception as e:
            print(e)

    def _search(self, parent, value):
        try:
            if parent is not None:
                if value == parent.value:
                    print("Value found!")
                elif value < parent.value:
                    self._search(parent.left, value)
                elif value > parent.value:
                    self._search(parent.right, value)
            else:
                print("Error at method: search()! Value not found!")
        except Exception as e:
            print(e)

    # Method to delete value from binary tree
    def delete(self, value):
        try:
            if self.root is None:
                print("Error at method: delete()! Tree is empty.")
            # If node to be deleted is root node
            elif self.root.value == value:
                if self.root.left is None and self.root.right is None:
                    self.root = None
                elif self.root.left and self.root.right is None:
                    self.root = self.root.left
                elif self.root.left is None and self.root.right:
                    self.root = self.root.right
                elif self.root.left and self.root.right:
                    parent_node = self.root
                    child_node = self.root.right
                    while child_node.left:
                        parent_node = child_node
                        child_node = child_node.left
                    self.root.value = child_node.value
                    if child_node.right:
                        if parent_node.value > child_node.value:
                            parent_node.left = child_node.right
                        elif parent_node.value < child_node.value:
                            parent_node.right = child_node.right
                    elif child_node.right is None:
                        if child_node.value < parent_node.value:
                            parent_node.left = None
                        else:
                            parent_node.right = None
            # If node to be deleted isn't root node
            parent = None
            child = self.root
            while child and child.value != value:
                parent = child
                if value < child.value:
                    child = child.left
                elif value > child.value:
                    child = child.right

            if child is None or child.value != value:
                print("Error at method: delete()! Value not found.")
            elif child.left is None and child.right is None:
                if value < parent.value:
                    parent.left = None
                else:
                    parent.right = None
            elif child.left and child.right is None:
                if value < parent.value:
                    parent.left = child.left
                else:
                    parent.right = child.left
            elif child.left is None and child.right:
                if value < parent.value:
                    parent.left = child.right
                else:
                    parent.right = child.right
            elif child.left and child.right:
                delNodeParent = child
                delNodeChild = child.right
                while delNodeChild.left:
                    delNodeParent = delNodeChild
                    delNodeChild = delNodeChild.left
                child.value = delNodeChild.value
                if delNodeChild.right:
                    if delNodeParent.value > delNodeChild.value:
                        delNodeParent.left = delNodeChild.right
                    else:
                        delNodeParent.right = delNodeChild.right
                else:
                    if delNodeParent.value > delNodeChild.value:
                        delNodeParent.left = None
                    else:
                        delNodeParent.right = None
        except Exception as e:
            print(e)

        
            
                    



