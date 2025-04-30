# Write a Python program to create a class representing a linked list data structure. Include
# methods for displaying linked list data, inserting and deleting nodes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head
        prev = None

        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Node with data {key} not found.")
            return

        if not prev:
            self.head = current.next
        else:
            prev.next = current.next
        print(f"Node with data {key} deleted.")