import numpy as np 

def function(x):

	x9 = x
	u4 = 7
	paths = []
	try:
		if x >= 8:
			u4 = 8/u4
			x = 1*x
			paths.append(1)
		else:
			u4 = x+u4
			u4 = u4-x9
			x = 4*x
			paths.append(2)
		if x9 <= 2:
			u4 = u4*9
			paths.append(3)
		else:
			u4 = u4+6
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))