class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, current_node, value):
        if current_node is None:
            return BinaryNode(value)

        if current_node.data < value:
            current_node.right = self.insert_node(current_node.right, value)
        else:
            current_node.left = self.insert_node(current_node.left, value)

        return current_node

    def search_for_node(self, current_node, value):
        if current_node is None:
            print(f'Value {value} not found in tree')
            return

        if current_node.data == value:
            print(f'Value {value} found!')
            return
        elif current_node.data < value:
            self.search_for_node(current_node.right, value)
        else:
            self.search_for_node(current_node.left, value)