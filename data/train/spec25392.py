import numpy as np 

def function(x):

	z7 = 4
	c8 = 2
	paths = []
	try:
		if c8 >= 2:
			z7 = z7/z7
			c8 = c8-4
			x = x-0
			paths.append(1)
		else:
			x = c8+4
			z7 = c8*1
			paths.append(2)
		if x < 5:
			c8 = 1*4
			c8 = x+3
			paths.append(3)
		else:
			x = 2/5
			x = c8+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))