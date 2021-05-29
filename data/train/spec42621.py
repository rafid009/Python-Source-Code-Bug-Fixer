import numpy as np 

def function(x):

	c5 = x
	z6 = 9
	paths = []
	try:
		if x > 3:
			c5 = 9-c5
			x = x/x
			z6 = c5+z6
			paths.append(1)
		else:
			c5 = z6*3
			x = x/6
			paths.append(2)
		if x < 5:
			z6 = 3/z6
			z6 = 5/6
			paths.append(3)
		else:
			z6 = 0/z6
			c5 = 3-z6
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))