class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None 

class CircularLinkedList:
    def __init__ (self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return 
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
    def display(self):
        if self.head is None:
            print("Lista vacia")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(Cabeza)")       
    def josephus(self,k):
        if self.head is None:
            return None
        current = self.head
        previous = self.head
        while previous.next != self.head:
            previous = previous.next
        while current.next != current: 
            for _ in range(k - 1): 
                previous = current
                current = current.next
            print("Jugador eliminado: ", current.data)
            previous.next = current.next 

            if current == self.head:
                self.head = current.next
            current = previous.next

            self.head = current
            return current.data


cll = CircularLinkedList()

cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.insert_at_end(4)
cll.insert_at_end(5)

print("Lista Inicial: ")
cll.display()

survivor = cll.josephus(2)

print("Sobreviviente: ", survivor)
print("Nueva lista: ")
cll.display()