# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array=[]
        cur=head
        while cur:
            array.append(cur.val)
            cur=cur.next

        l,r=0,len(array)-1
        while l<r:
            if array[l]==array[r]:
                l=l+1
                r=r-1
            else:
                return False
        return True




        