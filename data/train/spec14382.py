import numpy as np 

def function(x):

	z5 = x
	d5 = 2
	paths = []
	try:
		if d5 < 2:
			d5 = d5*3
			x = x+0
			z5 = 8+d5
			paths.append(1)
		else:
			z5 = 9*z5
			z5 = d5*8
			paths.append(2)
		if z5 >= 0:
			z5 = z5*1
			z5 = 5*z5
			x = 9-x
			paths.append(3)
		else:
			z5 = 3-z5
			x = x-7
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