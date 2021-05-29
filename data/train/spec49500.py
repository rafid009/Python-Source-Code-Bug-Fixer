import numpy as np 

def function(x):

	y0 = 0
	x6 = x
	paths = []
	try:
		if y0 <= 5:
			y0 = y0+x
			x = x+6
			paths.append(1)
		else:
			x6 = x6-4
			x6 = 7/x6
			paths.append(2)
		if y0 <= 1:
			x6 = x/x6
			x = y0*x
			y0 = y0+8
			paths.append(3)
		else:
			x = x/6
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