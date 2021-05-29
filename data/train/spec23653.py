import numpy as np 

def function(x):

	x9 = 4
	u4 = x
	paths = []
	try:
		if x9 < 1:
			x = x9*5
			u4 = x9-7
			x = x/9
			paths.append(1)
		else:
			x9 = u4/x9
			paths.append(2)
		if x >= 6:
			x9 = x9/x9
			u4 = u4-4
			u4 = 3+x9
			paths.append(3)
		else:
			x9 = 3*x9
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x9 = u4**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))