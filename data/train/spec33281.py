import numpy as np 

def function(x):

	c0 = x
	z4 = x
	paths = []
	try:
		if x <= 1:
			z4 = c0*z4
			paths.append(1)
		else:
			c0 = 3-c0
			z4 = 0+z4
			paths.append(2)
		if c0 >= 3:
			z4 = c0+7
			paths.append(3)
		else:
			z4 = c0/z4
			c0 = z4/7
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))