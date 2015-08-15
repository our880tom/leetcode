class Solution:
	def convert(self, s, numRows):
		result = ""
		if numRows == 1:
			return s
		for i in range(numRows):
			#print(i)
			offset = 2 * numRows -2
			for x in range(i,len(s), offset):
				if (x - i) % offset == 0:
					result = result + s[x]
					if  i != 0  and i != numRows - 1 and x + offset - 2*i < len(s):
						result = result + s[x + offset -2*i]
		return result








s =  Solution()
print(s.convert("ABCD", 3))
		