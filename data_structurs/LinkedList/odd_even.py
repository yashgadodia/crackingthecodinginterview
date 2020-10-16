# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd_tal = head
        even_head = head.next
        even_tail = even_head
        current_node = head.next.next
        current_position = 3

        while current_node:
            if current_position % 2 == 1:
                odd_tail.next = current_node
                
















# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None
 
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.last_node = None
 
#     def append(self, data):
#         if self.last_node is None:
#             self.head = Node(data)
#             self.last_node = self.head
#         else:
#             self.last_node.next = Node(data)
#             self.last_node = self.last_node.next
 
#     def display(self):
#         current = self.head
#         while current is not None:
#             print(current.data, end = ' ')
#             current = current.next
 
# a_llist = LinkedList()
# print('\n')
# for i in range(1,6):
#     a_llist.append(i)
# a_llist.display()
# print('\n')


