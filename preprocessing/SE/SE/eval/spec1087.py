import numpy as np 

def function(x):

	c6 = x
	s6 = x
	paths = []
	try:
		if s6 < 2:
			c6 = 2/3
			s6 = s6/s6
			paths.append(1)
		else:
			c6 = 1-x
			paths.append(2)
		if c6 >= 1:
			s6 = s6-5
			c6 = c6+s6
			s6 = s6+6
			paths.append(3)
		else:
			x = x*7
			c6 = x/8
			c6 = 4+1
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