import numpy as np 

def function(x):

	u4 = x
	j3 = 9
	paths = []
	try:
		if x >= 6:
			x = 6-x
			paths.append(1)
		else:
			u4 = 2-7
			u4 = j3-u4
			paths.append(2)
		if x >= 9:
			u4 = 6-j3
			u4 = u4+6
			u4 = x*3
			paths.append(3)
		else:
			u4 = x/6
			u4 = u4-8
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		j3 = u4**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))