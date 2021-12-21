class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(linked_list: Node) -> Node:
    main_pointer = linked_list
    prev_prev_main = main_pointer

    main_pointer = main_pointer.next
    prev_main = main_pointer

    main_pointer = main_pointer.next

    prev_prev_main.next = None

    while main_pointer is not None:
        prev_main.next = prev_prev_main

        prev_prev_main = prev_main
        prev_main = main_pointer

        main_pointer = main_pointer.next

    prev_main.next = prev_prev_main
    return prev_main


def print_linked_list(linked_list: Node):
    pointer = linked_list

    print('\nLinked List: ', end='')
    while pointer is not None:
        print(pointer.val, end=' ')
        pointer = pointer.next

    print()


if __name__ == '__main__':
    linked_list = Node(1)
    linked_list.next = Node(2)
    linked_list.next.next = Node(3)
    linked_list.next.next.next = Node(4)
    linked_list.next.next.next.next = Node(5)

    print_linked_list(linked_list)
    linked_list = reverse(linked_list)
    print_linked_list(linked_list)
