import numpy as np 

def function(x):

	y1 = x
	z3 = 4
	paths = []
	try:
		if y1 <= 4:
			y1 = y1+8
			z3 = 4*y1
			y1 = 2/y1
			paths.append(1)
		else:
			z3 = z3*y1
			y1 = y1/8
			z3 = z3-z3
			paths.append(2)
		if z3 <= 4:
			x = x/x
			x = y1/x
			x = x*8
			paths.append(3)
		else:
			z3 = 0+z3
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		z3 = y1**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))