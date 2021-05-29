import numpy as np 

def function(x):

	x4 = x
	x1 = 2
	paths = []
	try:
		if x1 <= 3:
			x4 = x4/1
			x4 = x4*3
			x = 3/x
			paths.append(1)
		else:
			x4 = x4/2
			paths.append(2)
		if x < 8:
			x = 0*6
			x = x-x
			x4 = x4+6
			paths.append(3)
		else:
			x4 = x1-x4
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))