# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

		if head.next == None:
			return None

		node = head
		length = 0

		while node != None:

			length = length + 1
			node = node.next

		mid_point = length // 2
		new_node = head

		while mid_point > 1:
			new_node = new_node.next
			mid_point = mid_point - 1

		new_node.next = new_node.next.next

		return head