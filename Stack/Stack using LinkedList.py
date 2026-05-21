class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            print(data,"added to stack")
        else:
            new_node.next = self.top
            self.top = new_node
            print(data,"added to stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        else:
            temp = self.top.data
            self.top = self.top.next
            print(temp,"removed from stack")
            del temp

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("top element is ",self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        else:
            print("==== Stack is =====")
            temp = self.top
            while temp is not None:
                print(temp.data)
                temp = temp.next

s = Stack()

while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            element = int(input("Enter element to push: "))
            s.push(element)

        elif choice == 2:
            s.pop()

        elif choice == 3:
            s.peek()

        elif choice == 4:
            s.display()

        elif choice == 5:
            print("Thank you for using this program")
            break

        else:
            print("Invalid choice")

