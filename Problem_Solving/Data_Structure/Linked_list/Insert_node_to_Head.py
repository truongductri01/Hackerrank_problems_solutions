# Link: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
input_txt = '''
5
383
484
392
975
321
'''

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        string = ""
        current = self.head
        while current != None:
            string += str(current.data) + "\n"
            current = current.next
        return string


def insertNodeAtHead(head, data):
    node = SinglyLinkedListNode(data)
    if head == None:
        return node
    else:
        current = head
        head = node
        head.next = current
        return head
        # while current.next != None:
        #     current = current.next
        # else:
        #     current.next = node
        #     return head  # as we need to point to the head of the llist every time we input new node


if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    print(llist)
