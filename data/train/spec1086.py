import numpy as np 

def function(x):

	x0 = x
	y0 = 9
	x = x
	paths = []
	try:
		if x0 <= 9:
			x0 = x0+x0
			paths.append(1)
		else:
			y0 = 8-y0
			x = x-9
			paths.append(2)
		if y0 > 1:
			y0 = y0+5
			y0 = y0*2
			x0 = 7*2
			paths.append(3)
		else:
			y0 = 6-7
			x0 = x0*x
			x0 = 3-x0
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