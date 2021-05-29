import numpy as np 

def function(x):

	x0 = x
	y0 = 2
	paths = []
	try:
		if x0 > 4:
			x = x/x0
			paths.append(1)
		else:
			x = 3*9
			y0 = x0/4
			paths.append(2)
		if x >= 2:
			x0 = x0+x
			x = 3/x0
			x0 = x0*1
			paths.append(3)
		else:
			x = x0*x
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