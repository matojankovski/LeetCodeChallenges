class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, ):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        pass



    def printll(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        itr = self.head
        llst = ""
        while itr:
            llst += str(itr.data) + "-->"
            itr = itr.next
        print(llst)



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(1)
    ll.insert_at_begining(5)
    ll.printll()





