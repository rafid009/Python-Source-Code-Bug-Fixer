import numpy as np 

def function(x):

	c3 = x
	z0 = x
	paths = []
	try:
		if x <= 7:
			z0 = x/5
			z0 = z0+x
			paths.append(1)
		else:
			c3 = c3*2
			paths.append(2)
		if c3 <= 9:
			z0 = 4-z0
			paths.append(3)
		else:
			x = 0+x
			c3 = 2+z0
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		z0 = c3**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))