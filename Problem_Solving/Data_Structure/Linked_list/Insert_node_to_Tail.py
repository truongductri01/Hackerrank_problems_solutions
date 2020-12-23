#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        string = ""
        current = self.head
        while current != None:
            string += str(current.data) + "\n"
            current = current.next
        return string


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if head == None:
        return node
    else:
        current = head
        while current.next != None:
            current = current.next
        else:
            current.next = node
            return head  # as we need to point to the head of the llist every time we input new node


if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head
    print(llist)

    # print_singly_linked_list(llist.head, '\n')
