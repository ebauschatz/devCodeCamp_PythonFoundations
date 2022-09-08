from platform import node


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node

    def find_node(self, node_value):
        current_node = self.head
        while current_node.value != node_value:
            if current_node.next is None:
                return False
            current_node = current_node.next
        return True