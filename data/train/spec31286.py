import numpy as np 

def function(x):

	c4 = 9
	z6 = 3
	paths = []
	try:
		if z6 > 5:
			x = x*0
			c4 = 3-z6
			paths.append(1)
		else:
			z6 = 9-x
			c4 = c4+1
			paths.append(2)
		if c4 > 2:
			x = 8+c4
			c4 = 4*z6
			paths.append(3)
		else:
			z6 = 3/z6
			z6 = 2*z6
			c4 = 5/c4
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