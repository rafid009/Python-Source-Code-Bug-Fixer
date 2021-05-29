import numpy as np 

def function(x):

	y1 = 7
	v7 = 4
	paths = []
	try:
		if x > 6:
			v7 = v7/x
			v7 = x-6
			x = x/5
			paths.append(1)
		else:
			y1 = v7/y1
			x = x-9
			paths.append(2)
		if x >= 1:
			x = x+y1
			v7 = 6*3
			paths.append(3)
		else:
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))