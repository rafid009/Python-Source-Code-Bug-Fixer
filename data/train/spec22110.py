import numpy as np 

def function(x):

	z4 = 6
	c3 = x
	x = 3
	paths = []
	try:
		if c3 > 8:
			z4 = z4+3
			paths.append(1)
		else:
			x = c3*x
			paths.append(2)
		if z4 <= 7:
			z4 = z4*2
			x = x-x
			paths.append(3)
		else:
			x = x+z4
			z4 = z4-c3
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))