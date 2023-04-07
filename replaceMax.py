#Q2--original list (12 95 140 110 40) new list (12 95 100 110 40),replace with max no
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def replace_max(self, new_data):
        if not self.head:
            return "List is empty!"
        max_node = self.head
        curr_node = self.head.next
        while curr_node:
            if curr_node.data > max_node.data:
                max_node = curr_node
            curr_node = curr_node.next
        max_node.data = new_data

    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


# create linked list
list1 = LinkedList()
list1.insert(12)
list1.insert(95)
list1.insert(140)
list1.insert(110)
list1.insert(40)

# replace maximum element with new value
list1.replace_max(100)

# display modified linked list
list1.display()

 
