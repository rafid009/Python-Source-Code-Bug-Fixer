import numpy as np 

def function(x):

	y1 = 6
	x3 = x
	paths = []
	try:
		if y1 > 0:
			x = 2*x
			y1 = 9/y1
			paths.append(1)
		else:
			x3 = x3*2
			paths.append(2)
		if y1 >= 2:
			y1 = 7/y1
			x = 2/x
			paths.append(3)
		else:
			x = 8/y1
			y1 = x*y1
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))