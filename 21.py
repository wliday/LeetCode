class Solution(object):
	def mergeTwoLists(self, l1, l2):
		if not l1:
			return l2
		if not l2:
			return l1

		pre = l3 = ListNode(0)

		while l1 and l2:
			if l1.val <= l2.val:
				l3.next = l1
				l1 = l1.next
			else:
				l3.next = l2
				l2 = l2.next
			l3 = l3.next

		if l1:
			l3.next = l1
		if l2:
			l3.next = l2

		return pre.next