import numpy as np 

def function(x):

	y0 = 3
	a8 = 1
	paths = []
	try:
		if x > 2:
			a8 = 3/3
			a8 = 4-a8
			paths.append(1)
		else:
			a8 = 8+6
			a8 = x*a8
			paths.append(2)
		if y0 >= 8:
			y0 = 9*7
			a8 = 0+9
			paths.append(3)
		else:
			y0 = y0-a8
			x = x/1
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