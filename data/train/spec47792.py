import numpy as np 

def function(x):

	x0 = 1
	y6 = x
	paths = []
	try:
		if y6 >= 8:
			y6 = y6+x0
			x0 = x0+8
			paths.append(1)
		else:
			y6 = y6*x
			paths.append(2)
		if x >= 1:
			y6 = y6-9
			y6 = x+y6
			paths.append(3)
		else:
			x0 = x0*y6
			x0 = x0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))