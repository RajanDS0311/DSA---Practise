class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left,data) #recursive function

        elif data > root.data:
            root.right = self.insert(root.right,data) #recursive function
        return root

    def search(self,root,key):
        if root is None:
            return False
        if key == root.data:
            return True
        elif key < root.data:
            return self.search(root.left,key)  #recursive function
        else:
            return self.search(root.right,key)  #recursive function

    def find_minimum(self,root): #delete function me use krne k liye
        while root.left is not None:
            root = root.left
        return root

    def delete(self,root,key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left,key)

        elif key > root.data:
            root.right = self.delete(root.right,key)

        else: #Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            #Node with two children
            temp = self.find_minimum(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,temp.data)

        return root

    # TRAVERSAL TECHNIQUES
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end = " ")
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.data,end = " ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end = " ")

bst = BinarySearchTree()
while True:
    print("\n--- Binary Search Tree Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = input("Enter your value: ")
        bst.root = bst.insert(bst.root,val)
        print("Node inserted")

    elif choice == 2:
        val = input("Enter your value: ")
        bst.root = bst.delete(bst.root,val)

    elif choice == 3:
        val = input("Enter your value: ")
        if bst.search(bst.root,val):
            print("Node found")
        else:
            print("Node not found")

    elif choice == 4:
        print("Inorder Traversal:")
        bst.inorder(bst.root)

    elif choice == 5:
        print("Preorder Traversal:")
        bst.preorder(bst.root)

    elif choice == 6:
        print("Postorder Traversal:")
        bst.postorder(bst.root)

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
