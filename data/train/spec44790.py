import numpy as np 

def function(x):

	c3 = x
	z2 = x
	paths = []
	try:
		if x <= 3:
			x = x+c3
			x = 3/4
			paths.append(1)
		else:
			x = 6/x
			z2 = 0*4
			paths.append(2)
		if x < 7:
			c3 = c3+x
			x = 2+9
			paths.append(3)
		else:
			x = z2*4
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c3 = c3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))