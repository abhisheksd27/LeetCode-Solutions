# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_in_A = set()
        
        current = headA
        while current:
            nodes_in_A.add(current)
            current = current.next
        
        current = headB
        while current:
            if current in nodes_in_A:
                return current
            current = current.next
        
        return None
