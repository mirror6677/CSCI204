class Node:
    data = None
    next = None

class SStack:
    def __init__(self):
        self.head = None

    def push(self, newNode):
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.head == None:
            return self.head

        else:
            popNode = self.head
            self.head = self.head.next
            return popNode
