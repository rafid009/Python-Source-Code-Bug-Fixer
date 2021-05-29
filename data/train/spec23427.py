import numpy as np 

def function(x):

	p3 = 2
	c5 = x
	paths = []
	try:
		if x > 4:
			x = 3*x
			p3 = 6/x
			p3 = 3/p3
			paths.append(1)
		else:
			x = 7+0
			x = x-8
			paths.append(2)
		if c5 < 1:
			c5 = c5/p3
			x = 8*6
			paths.append(3)
		else:
			x = p3-x
			p3 = 1/p3
			x = c5/x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))