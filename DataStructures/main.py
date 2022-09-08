from linked_list import LinkedList

class RunMain:
    def __init__(self):
        pass

    def run_linked_list_tasks(self):
        linked_list = LinkedList()
        linked_list.append_node(13)
        linked_list.append_node(42)
        linked_list.append_node(111)
        print(linked_list.find_node(111))

if __name__ == '__main__':
    main = RunMain()
    main.run_linked_list_tasks()