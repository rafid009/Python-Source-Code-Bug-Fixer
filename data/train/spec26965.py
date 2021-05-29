import numpy as np 

def function(x):

	c8 = 6
	s9 = x
	x = 8
	paths = []
	try:
		if s9 >= 0:
			c8 = 7-5
			paths.append(1)
		else:
			x = c8*x
			paths.append(2)
		if s9 < 7:
			c8 = 7-c8
			x = x+x
			s9 = s9*7
			paths.append(3)
		else:
			x = s9*c8
			c8 = s9-0
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		c8 = s9**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))