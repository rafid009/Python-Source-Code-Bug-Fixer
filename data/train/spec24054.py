import numpy as np 

def function(x):

	z9 = x
	c1 = x
	paths = []
	try:
		if x < 9:
			z9 = 7*z9
			paths.append(1)
		else:
			c1 = 8-6
			z9 = z9+0
			paths.append(2)
		if z9 <= 3:
			c1 = c1-9
			c1 = c1+c1
			z9 = z9*c1
			paths.append(3)
		else:
			z9 = 3*z9
			c1 = 4/1
			z9 = 7*5
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))