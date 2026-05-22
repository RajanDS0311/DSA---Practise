class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.front is None and self.rear is  None:
            self.front = new_node
            self.rear = new_node
            print(data, "is added to queue")
            return
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(data,"is added to queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        else:
            deleted = self.front.data
            self.front = self.front.next

        if self.front is None:
            self.rear = None
        print(deleted,"is deleted")

    def display(self):
        if self.front == None:
            print("Queue is empty")
            return
        else:
            temp = self.front
            while temp is not None:
                print(temp.data," -> ",end=" ")
                temp = temp.next
            print("None")
q = Queue()
while True:
    print("==== QUEUE MENU =====")
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. DISPALY")
    print("4. EXIT")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = int(input("Enter element: "))
        q.enqueue(element)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")