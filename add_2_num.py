# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str_l1 = ""
        str_l2 = ""
        while l1.next != None or l2.next != None: # NEED TO FIX THIS *** since l1 l2 can be different lengths
            str_l1 = str(l1.val)+ str_l1
            str_l2 = str(l2.val)+ str_l2
            # move on to next node
            l1 = l1.next
            l2 = l2.next
        
        # convert to int
        int_l1 = int(str_l1)
        int_l2 = int(str_l2)

        # save the sum into a list and reverse it 
        ls_l3 = list((str(int_l1 + int_l2)))
        reverse_l3 = ls_l3[::-1]

        # create dummy new node
        dummy = ListNode()
        for n in reverse_l3:
            curr = dummy
            nextNode = ListNode(n)
            curr.next = nextNode
            curr = curr.next

        return dummy.next