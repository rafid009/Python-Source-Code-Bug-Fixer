import numpy as np 

def function(x):

	x0 = x
	y6 = x
	paths = []
	try:
		if x > 8:
			x0 = x0/9
			paths.append(1)
		else:
			y6 = y6-x
			paths.append(2)
		if x0 < 4:
			x = x+6
			x0 = 4*x
			x0 = 0/7
			paths.append(3)
		else:
			x0 = 0+x
			y6 = y6/4
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