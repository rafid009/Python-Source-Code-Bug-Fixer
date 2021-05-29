import numpy as np 

def function(x):

	c5 = x
	z2 = 0
	paths = []
	try:
		if z2 <= 1:
			c5 = c5/7
			x = 4*7
			c5 = c5+2
			paths.append(1)
		else:
			x = 7/c5
			c5 = c5-7
			c5 = 6-c5
			paths.append(2)
		if c5 > 0:
			c5 = c5-5
			z2 = x+z2
			z2 = 0/8
			paths.append(3)
		else:
			c5 = z2*9
			c5 = 0+z2
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		z2 = c5**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))