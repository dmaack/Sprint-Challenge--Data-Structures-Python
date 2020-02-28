from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

# Append
    # if the storage length is less than the max capacity
        # add item to tail
        # set current to head
    # otherwise if at capacity
        # swap out the current value with incoming item
        # set current to next
        # if no current value
            # set current to head

    def append(self, item):
        if self.storage.__len__() < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.current.value = item
            self.current = self.current.next
            if self.current == None:
                self.current = self.storage.head


# GET
    # initalize a tracker 
    # while there is a node 
        # append the current node value to intialized tracker
        # move on to next node
    # return the list buffer contents


    def get(self):
        # Note:  This is the only [] allowed
        current_node = self.storage.head
        list_buffer_contents = []
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
