from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def convert(vals: List[int]) -> 'ListNode':
        list_node: ListNode = None
        prev: ListNode = None

        for val in vals:
            if list_node is None:
                list_node = ListNode(val)
                prev = list_node
            else:
                prev.next = ListNode(val)
                prev = prev.next
        return list_node

    def to_list(self) -> List[int]:
        int_list: List[int] = []
        curr = self
        while curr is not None:
            int_list.append(curr.val)
            curr = curr.next
        return int_list

    def __str__(self) -> str:
        return f"[{', '.join(list(map(lambda v: str(v), self.to_list())))}]"

class Solution:
    def addTwoNumbers(self, 
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        return None

class SolutionWithCarry (Solution):
    def addTwoNumbers(self,
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        base = 10
        sumNode: ListNode = None
        currNode: ListNode = None

        while l1 is not None or l2 is not None:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            sum = l1_val + l2_val + carry

            carry = int(sum / base)
            sum_val = sum % base
            
            if sumNode is None:
                sumNode = ListNode(sum_val)
                currNode = sumNode
            else:
                currNode.next = ListNode(sum_val)
                currNode = currNode.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            currNode.next = ListNode(carry)

        return sumNode


s: Solution = SolutionWithCarry()
# print(s.addTwoNumbers(ListNode.convert([0]), ListNode.convert([0])))
# print(s.addTwoNumbers(ListNode.convert([2,4,3]), ListNode.convert([5,6,4])))
print(s.addTwoNumbers(ListNode.convert([9,9,9,9,9,9,9]), ListNode.convert([9,9,9,9])))
