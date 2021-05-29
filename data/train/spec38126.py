import numpy as np 

def function(x):

	y0 = x
	n6 = 6
	paths = []
	try:
		if n6 < 0:
			x = x+n6
			n6 = 8+n6
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if n6 >= 6:
			x = x/n6
			x = 6/x
			n6 = n6-7
			paths.append(3)
		else:
			y0 = 4+y0
			x = x*y0
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