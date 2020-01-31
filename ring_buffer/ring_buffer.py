from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # set current node as head
        current_node = self.storage.head

        while current_node.next is not None:
            # add them to the lists
            list_buffer_contents.append(current_node.value)
            # set the pointer to the current node
            current_node = current_node.next

        list_buffer_contents.append(current_node.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
