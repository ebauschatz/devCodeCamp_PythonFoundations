from locale import currency
from exceptions import NoMatchingValueError

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

    def clear(self):
        #Python will garbage collect any unreferenced object, so no need to explicitly free memory
        while self.head is not None:
            self.head = self.head.next
        self.tail = None

    def add_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def remove(self, value_to_remove):
        current_node = self.head
        if current_node.value == value_to_remove:
            self.head = current_node.next
            return True
        
        next_node = self.head.next
        while next_node is not None:
            if next_node.value == value_to_remove:
                current_node.next = next_node.next
                if current_node.next is None:
                    self.tail = current_node
                return True
            else:
                current_node = next_node
                next_node = current_node.next
        return False

    def add_after(self, value_to_find, new_data):
        new_node = Node(new_data)
        current_node = self.head

        while current_node is not None:
            if current_node.value == value_to_find:
                if current_node.next is not None:
                    new_node.next = current_node.next
                else:
                    self.tail = new_node
                current_node.next = new_node
                return                
            else:
                current_node = current_node.next

        raise NoMatchingValueError(f'The value {value_to_find} was not found in the linked list.')
  
    def add_before(self, value_to_find, new_data):
        new_node = Node(new_data)
        if self.head.value == value_to_find:
            new_node.next = self.head
            self.head = new_node

        previous_node = self.head
        current_node = self.head.next
        while current_node is not None:
            if current_node.value == value_to_find:
                previous_node.next = new_node
                new_node.next = current_node
                return
            else:
                previous_node = current_node
                current_node = previous_node.next

        raise NoMatchingValueError(f'The value {value_to_find} was not found in the linked list.')