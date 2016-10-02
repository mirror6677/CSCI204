class Node:
    next = None
    data = None

class SLink:
    head = None
    elist = []
    size = 0

    def __init__(self, size=0):
        #?Come back and optimize startup
        pass

    def __len__(self):
        return self.size


    def add(self, value):
        #Adds a node to the head
        if(len(self.elist) > 0):
            newNode = self.elist.pop()
            newNode.data = value
            newNode.next = self.head
            self.head = newNode
            self.size += 1
        else:
            newNode = Node()
            newNode.next = self.head
            newNode.data = value
            self.head = newNode
            self.size += 1

    def remove(self, value):
        #Removes a node from the list
        prunner = None
        runner = self.head
        while runner != None and runner.data != value:
            prunner = runner
            runner = runner.next

        if runner == None:
            #It was not found, so no work to do
            return -1

        #Remove node
        if runner == self.head:
            #head case
            self.head = runner.next
            del runner
        else:
            #nonhead case
            prunner.next = runner.next
            del runner

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
