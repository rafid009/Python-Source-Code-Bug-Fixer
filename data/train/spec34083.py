import numpy as np 

def function(x):

	s5 = x
	c0 = x
	x = 8
	paths = []
	try:
		if x > 0:
			s5 = s5/x
			c0 = c0*c0
			paths.append(1)
		else:
			s5 = 2+3
			paths.append(2)
		if x > 2:
			s5 = c0*s5
			x = c0-x
			s5 = 6+s5
			paths.append(3)
		else:
			x = c0+x
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