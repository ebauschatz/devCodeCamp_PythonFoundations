from linked_list import LinkedList
from binary_node import BinaryNode

class RunMain:
    def __init__(self):
        pass

    def run_linked_list_tasks(self):
        linked_list = LinkedList()
        linked_list.append_node(13)
        linked_list.append_node(42)
        linked_list.append_node(111)
        print(linked_list.find_node(111))

    def run_binary_search_tree_tasks(self):
        root = BinaryNode(11)
        root.insert_node(root, 13)
        root.insert_node(root, 42)
        root.insert_node(root, 3)
        root.insert_node(root, 30)
        root.insert_node(root, 5)
        root.insert_node(root, 4)
        root.search_for_node(root, 5)
        root.search_for_node(root, 31)

if __name__ == '__main__':
    main = RunMain()
    #main.run_linked_list_tasks()
    main.run_binary_search_tree_tasks()