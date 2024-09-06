class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        num_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            if curr.val in num_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
