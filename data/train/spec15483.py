import numpy as np 

def function(x):

	x4 = x
	x3 = x
	paths = []
	try:
		if x3 < 2:
			x3 = x3*x3
			paths.append(1)
		else:
			x3 = 0-2
			x3 = x4-x4
			paths.append(2)
		if x3 < 1:
			x = 8+0
			x = x+x3
			paths.append(3)
		else:
			x = 4+3
			x = 6-0
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