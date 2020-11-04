import numpy as np

def find(matrix,obj_num):
	if matrix.shape == (0,0):
		return False    #用于排除特殊情况
	i = 0
	j = matrix.shape[0] - 1
	while i < matrix.shape[1] and j >= 0:
		if obj_num == int(matrix[j][i]):
			return True
		elif obj_num > int(matrix[j][i]):
			i = i+1
		else:
			j = j-1
	return False


if __name__ == '__main__':
	matrix = np.array([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
	obj_num = 15
	print(find(matrix,obj_num))