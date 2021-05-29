import numpy as np 

def function(x):

	c5 = 0
	z1 = 6
	paths = []
	try:
		if c5 >= 0:
			c5 = c5/x
			z1 = z1*z1
			paths.append(1)
		else:
			c5 = c5/7
			c5 = c5*3
			paths.append(2)
		if z1 <= 7:
			x = x/z1
			c5 = 6+z1
			paths.append(3)
		else:
			z1 = x+x
			z1 = 7*z1
			c5 = z1+z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))