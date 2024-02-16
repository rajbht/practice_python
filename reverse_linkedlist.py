from typing import Optional
from icecream import ic

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val}-->{self.next}" if self.next else f"{self.val}"

class Solution():
    def reverseList(self, head):
        new_list = None # new head of reversed list
        current_node = head # traverse the linked list
        # print(current_node)
        while current_node:
            next_node = current_node.next # track our position in original list
            # start building reversed list
            # ic(next_node)
            current_node.next = new_list # next pointer assigned to new_list
            # ic(current_node.next)
            new_list = current_node # current node is assigned to new_list
            # ic(new_list)
            current_node = next_node # next_node is assigned to current node
            # ic(current_node)

        # print(repr(new_list))
        return new_list

    def printList(self,curr):
        while curr:
            print(curr.val, "-->", end = '')
            curr = curr.next
        print()


head = ListNode([1,2,3,4,5]) # type: ignore

rev = Solution().reverseList(head)
Solution().printList(rev)

# ic(Solution().reverseList([]))