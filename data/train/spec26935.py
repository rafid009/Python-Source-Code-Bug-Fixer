import numpy as np 

def function(x):

	x3 = 7
	c2 = 2
	paths = []
	try:
		if c2 <= 0:
			x3 = c2*2
			x3 = 2/x
			x3 = 7*9
			paths.append(1)
		else:
			x3 = 3*x3
			c2 = 4*4
			paths.append(2)
		if x > 0:
			c2 = x/4
			paths.append(3)
		else:
			c2 = c2-x
			x3 = x3-x3
			c2 = c2*x
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		c2 = c2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))