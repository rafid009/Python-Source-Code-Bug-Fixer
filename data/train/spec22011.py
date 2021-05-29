import numpy as np 

def function(x):

	c6 = 0
	g9 = 6
	paths = []
	try:
		if c6 <= 6:
			g9 = x/g9
			c6 = 3+0
			g9 = 8+6
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if g9 >= 2:
			g9 = 6-g9
			c6 = c6*g9
			paths.append(3)
		else:
			g9 = g9*g9
			x = 2/x
			c6 = 7-c6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))