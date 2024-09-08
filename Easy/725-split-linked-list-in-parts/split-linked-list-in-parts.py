# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        

        def leng(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count

        def split_list(head, n):
            if not head:
                return None
            temp = head
            head = head.next
            for i in range(n-1):
                temp = temp.next
                head = head.next
            temp.next = None
            return head


        temp = head
        length = leng(temp)
        res = []


        while(temp):
            seg = math.ceil(length / k)
            length -= seg

            temp1 = temp
            temp = split_list(temp, seg)
            res.append(temp1)
            k -= 1
        
        while(k > 0):
            res.append(None)
            k -= 1
        
        return res