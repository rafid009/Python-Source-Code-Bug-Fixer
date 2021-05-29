import numpy as np 

def function(x):

	z9 = 7
	y0 = x
	paths = []
	try:
		if z9 > 2:
			y0 = 4+y0
			x = 4-z9
			paths.append(1)
		else:
			y0 = 5/y0
			paths.append(2)
		if x <= 7:
			x = x/x
			paths.append(3)
		else:
			z9 = x/y0
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