import numpy as np 

def function(x):

	c3 = 2
	g1 = x
	x = 4
	paths = []
	try:
		if x < 5:
			c3 = c3-x
			x = c3/x
			paths.append(1)
		else:
			g1 = g1-7
			paths.append(2)
		if x > 8:
			g1 = 0*g1
			paths.append(3)
		else:
			c3 = 6*g1
			x = 1*x
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