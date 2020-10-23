# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Brayden Brown

class LinkedList:

    def __init__(self, value=None):
        self.value = value
        self.next = self
        self.prev = self

    def is_sentinel(self):
        return self.value == None

    def is_empty(self):
        if self.next != self or self.prev != self:
            return False
        else:
            return True

    def is_last(self):
        return self.next.is_sentinel()

    def last(self):
        if self.is_last():
            return self
        else:
            return self.next.last()

    def append(self, attach_new_node):
        if self.is_sentinel():
           self.prev = attach_new_node
           attach_new_node.next =  self
           self = self.last()
           self.next = attach_new_node
           attach_new_node.prev = self
           return
        else:
            self.next.append(attach_new_node)
    
    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    pass
