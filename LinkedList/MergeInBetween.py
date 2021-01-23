class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        head = list1
        prev = None
        while(i<a and list1):
            prev = list1
            list1 = list1.next
            i += 1
        prev.next = list2
        while(a<=b):
            list1 = list1.next
            a += 1
        
        while(list2.next):
            list2 = list2.next
        list2.next = list1
        return head