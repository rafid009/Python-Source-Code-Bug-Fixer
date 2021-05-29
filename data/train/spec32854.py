import numpy as np 

def function(x):

	x1 = 1
	y6 = 6
	paths = []
	try:
		if x >= 0:
			x1 = x1*3
			paths.append(1)
		else:
			x = x+x
			x1 = 5*x
			paths.append(2)
		if y6 <= 5:
			x1 = x1/3
			x1 = x*5
			paths.append(3)
		else:
			x1 = 7-x
			y6 = y6*y6
			x1 = x*x
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