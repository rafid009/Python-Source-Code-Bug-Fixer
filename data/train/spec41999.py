import numpy as np 

def function(x):

	y0 = 6
	n4 = x
	paths = []
	try:
		if y0 > 0:
			n4 = 9*n4
			n4 = x/4
			paths.append(1)
		else:
			x = 1+y0
			paths.append(2)
		if y0 > 4:
			y0 = y0-n4
			y0 = y0*6
			paths.append(3)
		else:
			y0 = x+y0
			y0 = y0*0
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