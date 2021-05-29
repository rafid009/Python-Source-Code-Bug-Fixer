import numpy as np 

def function(x):

	c2 = x
	s1 = 2
	x = x
	paths = []
	try:
		if c2 >= 1:
			c2 = c2*2
			paths.append(1)
		else:
			x = 2/x
			s1 = s1+0
			paths.append(2)
		if c2 >= 5:
			c2 = c2*c2
			s1 = 2/2
			x = 3/x
			paths.append(3)
		else:
			c2 = c2+6
			c2 = c2/s1
			s1 = 4+5
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