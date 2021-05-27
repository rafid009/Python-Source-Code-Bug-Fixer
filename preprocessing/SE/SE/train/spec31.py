import numpy as np 

def function(x):

	z9 = x
	c4 = x
	paths = []
	try:
		if c4 <= 8:
			x = 2+x
			paths.append(1)
		else:
			c4 = c4/6
			z9 = z9/z9
			z9 = 9/z9
			paths.append(2)
		if z9 >= 0:
			c4 = 1*2
			z9 = c4+z9
			paths.append(3)
		else:
			z9 = 0/z9
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))