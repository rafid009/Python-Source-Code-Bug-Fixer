import numpy as np 

def function(x):

	s2 = 4
	c3 = x
	paths = []
	try:
		if c3 >= 2:
			x = 9-c3
			c3 = c3-c3
			s2 = s2/6
			paths.append(1)
		else:
			c3 = c3/9
			s2 = c3/5
			s2 = s2-c3
			paths.append(2)
		if x > 9:
			s2 = x-x
			s2 = 5+s2
			c3 = c3/6
			paths.append(3)
		else:
			x = x+6
			c3 = 5+c3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))