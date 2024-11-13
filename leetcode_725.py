class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return f"{nodes}"

    def add(self, new_data):
        new_node = Node(new_data)
        new_data.next = self.head
        self.head = new_node


    def len(self):
        node = self.head
        len = 0
        while node is not None:
            len += 1
            node = node.next
        return len





    # def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    #     pass


llist = LinkedList()



first_node = Node(1)
llist.head = first_node
second_node = Node(2)
third_node = Node(3)
first_node.next = second_node
second_node.next = third_node
print(llist)
print(llist.len())



