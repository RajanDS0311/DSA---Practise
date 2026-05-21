class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singly_LinkedList:
    def __init__(self):
        self.root = None  # global root for the linked list

    def createnew_node(self):
        a = int(input("Enter the data: "))
        return Node(a)

    def append(self):
        temp = self.createnew_node()
        if self.root is None:  # if list is empty
            self.root = temp
        else:
            current = self.root
            while current.next:
                current = current.next
            current.next = temp
        print(temp.data, "Data appended")

    def display(self):

        if self.root is None:
            print("List is empty")
            return
        current = self.root
        while current:
            print( current.data , "Address=", current.next , end=" ")
            current = current.next
        print()

    def count(self):
        if self.root is None:
            print("List is empty")
            return
        current = self.root
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def insert(self):
        newNode = self.createnew_node()
        p=int(input("Enter the position to insert: "))
        if p>=self.count():
            print("Invalid position")
            return
        elif p==0:
            newNode.next = self.root
            self.root = newNode
            print("Inserted successfully At beginning")
            return
        else :
            current = self.root
            for i in range(p):
                current = current.next

            newNode.next = current.next
            current.next = newNode
            print(newNode.data,"Inserted successfully  at ",p," position")




lin = Singly_LinkedList()

while True:
    i = int(input("Enter your choice \n1. append\n2. display\n3. exit\n4. Insert\n5. count\n "))
    if i == 1:
        lin.append()
    elif i == 2:
        lin.display()
    elif i == 3:
        break
    elif i == 4:
        lin.insert()
    elif i == 5:
        print("total nodes=", lin.count())
    else:
        print("Invalid choice")