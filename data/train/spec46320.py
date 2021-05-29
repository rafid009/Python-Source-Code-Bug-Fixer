import numpy as np 

def function(x):

	y0 = x
	z3 = 5
	paths = []
	try:
		if z3 <= 6:
			x = x/6
			y0 = y0*8
			paths.append(1)
		else:
			z3 = z3-9
			x = 6*7
			paths.append(2)
		if z3 < 2:
			y0 = y0/2
			paths.append(3)
		else:
			z3 = z3/y0
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		y0 = z3**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))