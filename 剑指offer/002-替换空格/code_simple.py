class Solution:
	def replaceSpace(self,s):
		s = s.replace(' ','%20')
		return s

if __name__ == '__main__':
	print(Solution().replaceSpace('We Are Happy'))