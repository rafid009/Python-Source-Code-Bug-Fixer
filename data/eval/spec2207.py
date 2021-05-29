import numpy as np 

def function(x):

	z7 = x
	c2 = x
	paths = []
	try:
		if c2 > 1:
			c2 = c2*4
			z7 = z7-2
			paths.append(1)
		else:
			c2 = 5*c2
			z7 = 6+z7
			x = z7+8
			paths.append(2)
		if c2 <= 4:
			z7 = z7-8
			x = 2-x
			x = c2+1
			paths.append(3)
		else:
			z7 = z7*5
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))