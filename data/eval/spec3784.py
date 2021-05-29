import numpy as np 

def function(x):

	c3 = 5
	l8 = 2
	paths = []
	try:
		if x > 5:
			l8 = x+l8
			paths.append(1)
		else:
			l8 = l8*1
			l8 = l8/6
			paths.append(2)
		if x >= 2:
			l8 = 2-l8
			c3 = c3/l8
			c3 = 7*c3
			paths.append(3)
		else:
			c3 = c3*c3
			x = x-8
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