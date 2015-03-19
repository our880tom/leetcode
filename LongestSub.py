class Solution:
	def lengthOfLongestSubstring(self,s):
		sum = 0
		count = 0
		start = 0
		map = {}
		for x in range(len(s)):
			if map.get(s[x]) != None:
				y = map.get(s[x])
				count = x - y
				for z in range(start,y + 1):
					del map[s[z]]
				start = y + 1
			else:
				count += 1

			map[s[x]] = x

			if count > sum:
				sum = count
		return sum