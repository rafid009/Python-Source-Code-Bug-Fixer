import numpy as np 

def function(x):

	u6 = x
	y7 = 8
	x = 7
	paths = []
	try:
		if y7 >= 0:
			y7 = 4-y7
			paths.append(1)
		else:
			u6 = u6+u6
			u6 = u6/u6
			y7 = y7/x
			paths.append(2)
		if x >= 3:
			x = 4+6
			x = x+8
			paths.append(3)
		else:
			u6 = u6-y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))