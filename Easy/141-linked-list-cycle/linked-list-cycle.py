# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()  # Create a set to store visited nodes
        
        current = head
        while current:
            if current in visited:  # If current node is already in visited set, a cycle is found
                return True
            visited.add(current)  # Add current node to visited set
            current = current.next  # Move to the next node
        
        return False  # No cycle found
