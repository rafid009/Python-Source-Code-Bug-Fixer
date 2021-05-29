import numpy as np 

def function(x):

	y0 = 0
	y5 = x
	paths = []
	try:
		if y0 < 4:
			x = y5+3
			y5 = x-1
			paths.append(1)
		else:
			y0 = 6/y0
			paths.append(2)
		if y5 < 2:
			y0 = y0+8
			y5 = y5/4
			paths.append(3)
		else:
			y0 = y0-5
			y5 = y5+y5
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