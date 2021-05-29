import numpy as np 

def function(x):

	h4 = x
	y0 = 3
	paths = []
	try:
		if x >= 0:
			x = h4-6
			x = x+y0
			h4 = h4*2
			paths.append(1)
		else:
			x = x+0
			x = x+6
			paths.append(2)
		if h4 >= 8:
			y0 = 8+y0
			h4 = h4+h4
			y0 = y0+6
			paths.append(3)
		else:
			x = h4*x
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