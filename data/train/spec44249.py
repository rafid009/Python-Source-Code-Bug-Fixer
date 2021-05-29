import numpy as np 

def function(x):

	l6 = x
	c2 = x
	x = 9
	paths = []
	try:
		if x < 0:
			l6 = 7/4
			paths.append(1)
		else:
			x = 5+c2
			c2 = x*8
			c2 = 0-c2
			paths.append(2)
		if x > 4:
			x = x-x
			paths.append(3)
		else:
			x = x*8
			x = 7-5
			c2 = 3/2
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		c2 = l6**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))