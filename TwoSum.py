class Solution:
	def _init_(self):
		pass
	def twoSum(self, num, target):
		print(num)
		map = {}
		i = 1
		for x in num:
			map[x] =  i
			i += 1
		print(map)

		mix = 0
		max = len(num) - 1
		print(max)

		num.sort()
		print(num)
		result = []
		for x in range(0, len(num)):
			if mix > max:
				break
			elif (num[mix] + num[max]) > target :
				max -= 1
			elif (num[mix] + num[max]) < target :
				mix += 1
			else :
				a = map[num[mix]]
				b = map[num[max]]
				print(a)
				print(b)
				if a > b:
					tmp = a
					a = b
					b = tmp
				result.append(a)
				result.append(b)
				break
		return result

a = [0, 4, 3, 0]
s = Solution()
print(s.twoSum(a, 0))
