# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s_length = len(s)
        space_count = 0
        for i in s:
            if i == ' ':
                space_count += 1
        new_length = s_length + space_count*2
        new_list = [' '] * new_length  #new_list并不是string,是数组格式
        j = 0
        for i in range(len(s)):
            if s[i] == ' ':
                new_list[j:j+3] = '%20'  #注意list的[起点，终点]，左闭右开原则
                j += 3
            else:
                new_list[j] = s[i]
                j += 1
        return ''.join(new_list)

if __name__ == '__main__':
	s = 'We Are'
	new_s = Solution().replaceSpace(s)
	print(new_s)