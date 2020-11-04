def find(matrix,obj_number):
	i = 0
	j = len(matrix[0])-1
	while j >= 0 and i < len(matrix[0]):
		print(matrix[j][i])
		if obj_number == matrix[j][i]:
			return j,i    # return语句将Python函数的结果，返回到调用的地方，并把程序的控制权一起返回，即会退出函数程序
		elif obj_number > matrix[j][i]:
			i = i + 1;
		else:
			j = j - 1;
	return False


if __name__ == '__main__':
	line1 = [1,2,8,9]
	line2 = [2,4,9,12]
	line3 = [4,7,10,13]
	line4 = [6,8,11,15]
	matrix = [line1,line2,line3,line4] #python的数据类型是列表，二维列表可以用numpy中的ndarray
	obj_number = 11
	print(find(matrix,obj_number))
	