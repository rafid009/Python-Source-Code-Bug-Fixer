import numpy as np 

def function(x):

	s2 = 3
	c9 = x
	paths = []
	try:
		if c9 > 4:
			c9 = s2/s2
			x = 7/1
			c9 = c9-4
			paths.append(1)
		else:
			c9 = 7-c9
			paths.append(2)
		if x > 2:
			x = x*5
			x = 5*9
			paths.append(3)
		else:
			s2 = s2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))