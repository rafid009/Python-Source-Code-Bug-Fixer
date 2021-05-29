import numpy as np 

def function(x):

	y0 = x
	z8 = x
	paths = []
	try:
		if x <= 4:
			x = 2+x
			paths.append(1)
		else:
			x = 1+x
			x = x-x
			paths.append(2)
		if x < 3:
			x = x+9
			x = z8/5
			z8 = z8-2
			paths.append(3)
		else:
			y0 = x*y0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		z8 = y0**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))