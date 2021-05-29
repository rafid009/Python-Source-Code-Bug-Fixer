import numpy as np 

def function(x):

	s5 = 8
	c1 = 7
	paths = []
	try:
		if x >= 9:
			x = x-9
			x = 3/1
			c1 = c1+2
			paths.append(1)
		else:
			c1 = 6-c1
			s5 = c1-6
			paths.append(2)
		if s5 <= 3:
			c1 = c1+1
			paths.append(3)
		else:
			x = c1/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))