import numpy as np 

def function(x):

	y3 = x
	y0 = 7
	paths = []
	try:
		if x >= 5:
			y0 = y0*y3
			x = x-8
			paths.append(1)
		else:
			x = 3*5
			x = x*y0
			paths.append(2)
		if x <= 3:
			y0 = x-9
			paths.append(3)
		else:
			x = 0-8
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y3 = y0**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))