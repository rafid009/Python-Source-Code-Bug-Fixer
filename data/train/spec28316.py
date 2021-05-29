import numpy as np 

def function(x):

	c4 = 9
	z4 = 3
	paths = []
	try:
		if c4 > 0:
			z4 = 5*1
			z4 = c4*1
			z4 = x-7
			paths.append(1)
		else:
			z4 = c4+9
			paths.append(2)
		if x > 0:
			c4 = 8-2
			c4 = z4*c4
			x = x-1
			paths.append(3)
		else:
			x = 7/x
			x = x+x
			c4 = 1*9
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))