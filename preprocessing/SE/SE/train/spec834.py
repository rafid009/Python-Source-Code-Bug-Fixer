import numpy as np 

def function(x):

	c3 = x
	s5 = x
	paths = []
	try:
		if s5 > 9:
			x = s5-c3
			c3 = c3/s5
			c3 = 7*4
			paths.append(1)
		else:
			s5 = s5*6
			paths.append(2)
		if x > 9:
			s5 = 4*s5
			paths.append(3)
		else:
			s5 = 6-s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		c3 = s5**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))