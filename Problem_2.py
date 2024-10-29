## This is my solution for the Add Two Numbers Problem, where the numbers are in Linked List format

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode(0) # Since the result has to be a Linked List as well
        final = temp # Added a temporary and a final pointer to the answer

        total_sum = 0 # This is the total sum of l1[i] + l2[j] where i == j or i != j 
        carry_forward = 0 # This is incase l1[i] + l2[j] >= 10

        while l1 or l2 or carry_forward:
            total_sum = carry_forward # This is to take any carry forward from the previous addition if it exists otherwise will be 0

            if l1:
                total_sum += l1.val
                l1 = l1.next

            if l2:
                total_sum += l2.val
                l2 = l2.next
                
            carry_forward = total_sum // 10 # to check if carry forward exists else will have value of 0
            number = total_sum % 10 # to get the final number of the output

            # To add the number to our temporary list in Linked List format
            temp.next = ListNode(number) 
            temp = temp.next
        
        # Since the final pointer points to the first temp node, we can return the rest of it by using final.next
        return final.next

        
        