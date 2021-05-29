import numpy as np 

def function(x):

	c8 = 6
	z9 = x
	paths = []
	try:
		if z9 >= 4:
			z9 = z9+z9
			c8 = c8-3
			x = 5*c8
			paths.append(1)
		else:
			z9 = c8/1
			c8 = c8+7
			c8 = 2-5
			paths.append(2)
		if x < 4:
			c8 = 1+6
			c8 = z9-c8
			c8 = c8*3
			paths.append(3)
		else:
			x = 8*z9
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		z9 = c8**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))