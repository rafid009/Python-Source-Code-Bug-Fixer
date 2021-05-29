import numpy as np 

def function(x):

	z4 = 6
	c2 = 8
	x = x
	paths = []
	try:
		if z4 <= 4:
			c2 = c2-0
			z4 = x/z4
			paths.append(1)
		else:
			z4 = z4-c2
			z4 = 8/7
			paths.append(2)
		if x <= 3:
			x = x+8
			c2 = 9+z4
			x = x/2
			paths.append(3)
		else:
			x = x*2
			c2 = 7+z4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))