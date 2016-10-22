import sStack

class Node:
    next = None
    data = []

class SLink:
    def __init__(self, size=0):
        self.head = None
        self.pStack = sStack()

        for i in range(size):
            sStack.push(None)

        self.size = 0

    def __len__(self):
        return self.size


    def add(self, valueList):
        #Adds a node to the head
        if(self.pStack.head != None):
            newNode = self.pStack.pop()

            for value in valueList:
                newNode.data.append(value)

            newNode.next = self.head
            self.head = newNode
            self.size += 1
        else:
            newNode = Node()
            newNode.next = self.head

            for value in valueList:
                newNode.data.append(value)

            self.head = newNode
            self.size += 1

    def remove(self, value):
        #Removes a node from the list
        prunner = None
        runner = self.head
        while runner != None and runner.data[0] != value:
            prunner = runner
            runner = runner.next

        if runner == None:
            #It was not found, so no work to do
            return -1

        if runner == self.head:
            #head case
            self.head = runner.next
        else:
            #nonhead case
            prunner.next = runner.next

        #Empty node and push onto the stack
        runner.data = []
        runner.next = None
        pStack.push(runner)

    def __iter__(self):
        return SLinkIterator(self.head)


class SLinkIterator:

    def __init__(self, head):
        self.runner = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.runner == None:
            raise StopIteration
        else:
            item = self.runner.data
            self.runner = self.runner.next
            return item
