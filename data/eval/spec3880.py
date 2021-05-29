import numpy as np 

def function(x):

	d0 = x
	y0 = x
	x = 9
	paths = []
	try:
		if d0 < 0:
			d0 = d0+x
			d0 = d0-y0
			d0 = x+d0
			paths.append(1)
		else:
			y0 = 6/y0
			x = 7-x
			paths.append(2)
		if d0 <= 8:
			y0 = 0-8
			y0 = 5+x
			y0 = 1-x
			paths.append(3)
		else:
			d0 = 5+7
			d0 = d0*x
			y0 = d0/y0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y0 = x**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))