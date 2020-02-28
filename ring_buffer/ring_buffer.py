from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

# Append
    # if the storage length is less than the max capacity
        # add item to tail
    # otherwise 
        # if no node
            # add item to the head 
            # set current to head
        # Otherwise
            # if next of current
                # insert item after head / current 
                # set current as next
                # delete the 'next' / item it is replacing
            # otherwise if at end of list / back to begining of ring
                # remove item from the head
                # add the current item to the head
                # set the current 'index' to head
    def append(self, item):
        pass 

# GET
    # initalize a tracker
    # while there is a begining 
        # assign list buffer content the values of of the tracker
    # return the list buffer contents


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
