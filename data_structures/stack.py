"""
## Stack

One-ended linear data structure which models a real world stack by
having two primary operations, pop and push.

Usage:

- Used by undo mechanisms in text editors
- Used in compiler syntax checking for matching brackets and braces
- Used behind the scenes to support recursion by keeping track of 
  previous function calls.
- Used for Depth First Search (DFS)
"""
from nodes import Node


class Stack:
    def __init__(self):
        self.head = None

    def __str__(self):
        output = ""

        currNode = self.head
        while currNode:
            output += f"{currNode.value} "
            currNode = currNode.next

        return output.strip()

    def pop(self):
        removedNode = self.head
        if self.head:
            self.head = self.head.next
        return removedNode

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
