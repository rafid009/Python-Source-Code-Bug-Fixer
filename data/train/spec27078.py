import numpy as np 

def function(x):

	y0 = x
	a2 = x
	paths = []
	try:
		if a2 > 5:
			x = x-3
			a2 = a2/a2
			y0 = a2*8
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if y0 >= 6:
			y0 = x+y0
			y0 = y0*y0
			x = 6*x
			paths.append(3)
		else:
			x = a2*5
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y0 = y0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))