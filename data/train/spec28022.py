import numpy as np 

def function(x):

	s0 = 8
	c9 = 5
	paths = []
	try:
		if x > 2:
			x = x-8
			paths.append(1)
		else:
			x = x+c9
			c9 = 9+c9
			paths.append(2)
		if x > 8:
			s0 = x/s0
			c9 = 2/x
			paths.append(3)
		else:
			s0 = x*s0
			s0 = s0/7
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))