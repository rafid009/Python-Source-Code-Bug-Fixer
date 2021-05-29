import numpy as np 

def function(x):

	u4 = 7
	j4 = x
	paths = []
	try:
		if u4 >= 5:
			u4 = u4*u4
			paths.append(1)
		else:
			x = u4/8
			u4 = 6*9
			paths.append(2)
		if j4 < 4:
			u4 = 4+u4
			paths.append(3)
		else:
			u4 = 7/u4
			x = j4*u4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))