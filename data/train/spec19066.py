import numpy as np 

def function(x):

	y0 = x
	o4 = 4
	paths = []
	try:
		if x > 8:
			y0 = y0-7
			y0 = 6/6
			o4 = o4-x
			paths.append(1)
		else:
			x = 8/y0
			o4 = y0+6
			y0 = y0/y0
			paths.append(2)
		if y0 <= 7:
			y0 = o4+y0
			paths.append(3)
		else:
			o4 = 7-o4
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