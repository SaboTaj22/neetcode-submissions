# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # prev trails behind curr, starting as None since the new tail points to nothing

        while curr: # Iterate until we've gone past the last node
            temp = curr.next # Save the next node before we overwrite the pointer
            curr.next = prev # Reverse the pointer so the current node points backward
            prev = curr # Move prev forward to the current node
            curr = temp # Move curr forward to the saved next node
        return prev # When curr is None, prev is sitting on the old tail, which is the new head

        # Time Complexity: O(n)
        # Space Complexity: O(1)