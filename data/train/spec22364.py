import numpy as np 

def function(x):

	c9 = 8
	c3 = 5
	x = x
	paths = []
	try:
		if c3 < 7:
			c3 = x*c9
			c3 = c3*8
			paths.append(1)
		else:
			c3 = 7-8
			x = x*x
			paths.append(2)
		if c3 <= 7:
			c9 = c9*c3
			x = 2+x
			x = 7+2
			paths.append(3)
		else:
			c3 = 7/c3
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