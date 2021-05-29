import numpy as np 

def function(x):

	z4 = x
	c2 = x
	paths = []
	try:
		if x > 9:
			c2 = c2-5
			z4 = 9*c2
			paths.append(1)
		else:
			z4 = c2/3
			x = c2-c2
			z4 = c2-5
			paths.append(2)
		if x >= 1:
			z4 = z4-6
			c2 = c2/3
			x = x+x
			paths.append(3)
		else:
			x = x*c2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))