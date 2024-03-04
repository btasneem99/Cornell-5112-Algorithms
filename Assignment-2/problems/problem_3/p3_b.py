'''
Problem 3b
'''
import random


class Node: 
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level
        self.level = level


class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.sentinel = Node(None, self.max_level)
        self.root = None

    def set_level(self):
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, x: int) -> None:
        new_node_level = self.set_level()
        new_node = Node(x, new_node_level)
        curr = self.sentinel
        for level in range(self.max_level - 1, -1, -1):
            while curr.next[level] and curr.next[level].val < x:
                curr = curr.next[level]
            if level < new_node_level:
                new_node.next[level] = curr.next[level]
                curr.next[level] = new_node
        if curr == self.sentinel:
            self.root = new_node

    def delete(self, x: int) -> None:
        curr = self.sentinel
        prev = curr
        for level in range(self.max_level - 1, -1, -1):
            while curr.next[level] and curr.next[level].val <= x:
                if curr.val == x:
                    break
                prev = curr
                curr = curr.next[level]

            if curr and curr.val == x:
                while prev.next[level] and prev.next[level].val < x:
                    prev = prev.next[level]
                prev.next[level] = curr.next[level]
        if curr == self.root:
            self.root = curr.next[0]
   
    def search(self, x: int) -> Node:
        curr = self.sentinel
        for level in range(self.max_level - 1, -1, -1):
            while curr.next[level] and curr.next[level].val <= x:
                curr = curr.next[level]
            if curr.val is not None and curr.val == x:
                return curr