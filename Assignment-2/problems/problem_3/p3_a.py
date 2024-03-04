'''
Problem 3a
'''


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, x):
        new_node = Node(x)
        if self.root is None or x < self.root.val:
            new_node.next = self.root
            self.root = new_node
        else:
            current = self.root
            while current.next is not None and current.next.val < x:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def search(self, x):
        current = self.root
        while current is not None and current.val < x:
            current = current.next
        if current is not None and current.val == x:
            return current
        return None

    def delete(self, x):
        if self.root is None:
            return

        if self.root.val == x:
            self.root = self.root.next
            return

        current = self.root
        while current.next is not None and current.next.val < x:
            current = current.next
        if current.next is not None and current.next.val == x:
            current.next = current.next.next

# This code provides a complete implementation of a sorted linked list with the insert, search, and delete methods.
# The runtime complexities are similar to the previous explanation:
# - Search: O(n) in the worst case and O(1) in the best case.
# - Insertion: O(n) in the worst case and O(1) in the best case.
# - Deletion: O(n) in the worst case and O(1) in the best case.