import numpy as np 

def function(x):

	b8 = 3
	y1 = 3
	paths = []
	try:
		if b8 > 1:
			y1 = x-y1
			paths.append(1)
		else:
			b8 = 9-b8
			x = 7-x
			x = 9*x
			paths.append(2)
		if b8 > 2:
			y1 = 0+9
			paths.append(3)
		else:
			y1 = y1-b8
			y1 = b8*9
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