class ListNode:
	
	def __init__(self, x):
		self.val = x
		self.next = None



class Solution:

	def addTwoNumbers(self, l1, l2):
		res = ListNode(0)
		cur = res

		sum = 0
		while True:
			if l1 != None:
				sum += l1.val
				l1 = l1.next
			if l2 != None:
				sum += l2.val
				l2 = l2.next

			cur.val = sum % 10
			sum /= 10

			if l1 != None or l2 != None or sum != 0:
				cur.next = ListNode(0)
				cur = cur.next
			else:
				break

		return res

t1 = ListNode(2)
t2 = ListNode(4)
t3 = ListNode(3)
t1.next = t2
t2.next = t3

t4 = ListNode(5)
t5 = ListNode(6)
t6 = ListNode(4)
t4.next = t5
t5.next = t6

s = Solution()
print(s.addTwoNumbers(t1, t4).val)
print(s.addTwoNumbers(t1, t4).next.val)
print(s.addTwoNumbers(t1, t4).next.next.val)

		