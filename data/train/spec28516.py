import numpy as np 

def function(x):

	c1 = 5
	s2 = x
	x = 4
	paths = []
	try:
		if s2 <= 1:
			c1 = x-c1
			paths.append(1)
		else:
			x = x-9
			c1 = c1+6
			paths.append(2)
		if s2 > 2:
			x = 5-3
			c1 = c1+c1
			s2 = 2-c1
			paths.append(3)
		else:
			x = x*2
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