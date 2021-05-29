import numpy as np 

def function(x):

	b3 = x
	y0 = x
	paths = []
	try:
		if x >= 2:
			x = y0/x
			paths.append(1)
		else:
			y0 = 3*y0
			x = 3-x
			y0 = y0*9
			paths.append(2)
		if x <= 0:
			y0 = 8/y0
			y0 = x*y0
			paths.append(3)
		else:
			x = x/b3
			b3 = x*b3
			b3 = 2+9
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