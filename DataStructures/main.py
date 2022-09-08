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
        root = BinaryNode(27)
        root.insert_node(root, 14)
        root.insert_node(root, 35)
        root.insert_node(root, 10)
        root.insert_node(root, 19)
        root.insert_node(root, 31)
        root.insert_node(root, 42)

        print('\nInorder Display:')
        root.inorder_tree_display(root)
        print('\nPreorder Display:')
        root.preorder_tree_display(root)
        print('\nPostorder Display:')
        root.postorder_tree_display(root)
        # root.search_for_node(root, 5)
        # root.search_for_node(root, 30)
        print()

if __name__ == '__main__':
    main = RunMain()
    #main.run_linked_list_tasks()
    main.run_binary_search_tree_tasks()