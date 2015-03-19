class solution:
	# @return a float
	def findMedianSortedArrays(self, A, B):
		sum = len(A) + len(B)
		print(sum)
		if sum % 2 == 1:
			return self.findKth(A, B, sum / 2 + 1)
		else:
			return (self.findKth(A, B, sum / 2) + self.findKth(A, B, sum / 2 + 1)) / 2.0

	def findKth(self, A, B, k):
		if len(A) > len(B):
			return self.findKth(B, A, k)
		if len(A) == 0:
			return B[k - 1]
		if k == 1:
			return min(A[0], B[0])

		pa = min(len(A), k /2)
		pb = k - pa

		print(A)
		print(B)
		print(pa)
		print(pb)

		if (A[pa - 1] < B[pb -1]):
			return self.findKth(A[pa:], B, k - pa)
		elif (A[pa - 1] > B[pb -1]):
			return self.findKth(A, B[pb:], k - pb)
		else:
			return A[pa - 1]
		


s = solution()
print(s.findMedianSortedArrays([1],[2,3]))