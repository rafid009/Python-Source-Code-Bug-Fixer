import numpy as np 

def function(x):

	d8 = x
	y0 = x
	paths = []
	try:
		if x >= 3:
			y0 = y0/9
			d8 = 2/7
			y0 = y0-x
			paths.append(1)
		else:
			d8 = 8*d8
			y0 = y0+y0
			paths.append(2)
		if y0 >= 9:
			y0 = 2*y0
			paths.append(3)
		else:
			d8 = 7/8
			x = x+d8
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))