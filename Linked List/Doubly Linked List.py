class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.root = None

    def insert_at_front(self,data):
        new_node = Node(data)

        if self.root is None:
           self.root = new_node
        else:
            new_node.next = self.root
            self.root.prev = new_node
            self.root = new_node
        print(data, " added at begining of Linked List")

    def insert_at_back(self,data):
        new_node = Node(data)
        if self.root is None:
           self.root = new_node
           return
        temp = self.root
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print(data, " added at end of Linked List")

    def count(self):
        if self.root is None:
            print("Linked List is empty")
            return
        temp = self.root
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert_in_between(self,data):
        new_node = Node(data)
        p = int(input("Enter the position: "))
        if p < 0 or p > self.count():
            print("Invalid Position")
            return
        elif p == 0:
            new_node.next = self.root
            if self.root is not None:
                self.root.prev = new_node
            self.root = new_node
            return
        else:
            temp = self.root
            for i in range(p -1):
                temp = temp.next

            new_node.next = temp.next # Connection part of new node
            new_node.prev = temp

            if temp.next: #jaha insert krna hai uske aage wale node ka connection
                temp.next.prev = new_node
            temp.next = new_node

    def delete_element(self,data):
        temp = self.root
        while temp is not None and temp.data != data:
            temp = temp.next
        if temp is None:
            print("Element Not Found")
            return

        if temp.prev is None: #if deleting first node
            self.root = temp.next

            if self.root is not None:
                self.root.prev = None
        else:
            temp.prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = temp.prev
        del temp
        print(data," deleted from Linked List")

    def search(self,data):
        temp = self.root
        p = 0
        while temp:
            if temp.data == data:
                print(data," is Found at position ",p)
                return
            temp = temp.next
            p = p + 1

        print("Element Not Found")

    def display(self):
        temp = self.root
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        if self.root is None:
            print("Linked List is empty")
            return
        else:
            temp = self.root
            while temp.next:
                temp = temp.next

            while temp:
                print(temp.data," <-> ",end = ' ')
                temp = temp.prev
        print("None")

dll = DoublyLinkedList()

while True:
    print("\n--- Doubly Linked List ---")
    print("1. Insert at beginning of Linked List")
    print("2. Insert at end of Linked List")
    print("3. Insert in between Linked List")
    print("4. Display")
    print("5. Search")
    print("6. Display Backward")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        data=int(input("Enter the data: "))
        dll.insert_at_front(data)

    elif choice == 2:
        data=int(input("Enter the data: "))
        dll.insert_at_back(data)

    elif choice == 3:
        data=int(input("Enter the data: "))
        dll.insert_in_between(data)

    elif choice == 4:
        dll.display()

    elif choice == 5:
        data=int(input("Enter the data: "))
        dll.search(data)

    elif choice == 6:
        dll.display_backward()

    elif choice == 7:
        print("Thank you for using this program")
        break

    else:
        print("Invalid Choice")