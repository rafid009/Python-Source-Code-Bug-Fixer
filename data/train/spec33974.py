import numpy as np 

def function(x):

	s6 = 9
	c1 = 8
	paths = []
	try:
		if c1 < 4:
			x = x-9
			paths.append(1)
		else:
			c1 = c1*8
			c1 = 6/c1
			paths.append(2)
		if c1 <= 3:
			c1 = c1*s6
			paths.append(3)
		else:
			s6 = 7-x
			x = c1+x
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