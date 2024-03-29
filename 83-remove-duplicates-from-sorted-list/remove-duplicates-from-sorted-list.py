class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headd = head
        while headd != None and headd.next != None:
            temp = headd.next
            if headd.val == temp.val:
                headd.next =  temp.next
            else:
                headd = headd.next
        return head
                