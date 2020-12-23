# Link: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        return self.head


# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        # current = llist.head
        # # print(current)
        # while current != None:
        #     print(current.data)
        #     current = current.next

        llist.reverse()
        current = llist.head
        while current != None:
            print(current.data)
            current = current.next
