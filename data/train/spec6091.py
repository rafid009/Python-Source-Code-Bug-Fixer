import numpy as np 

def function(x):

	c0 = x
	s2 = x
	paths = []
	try:
		if s2 <= 4:
			c0 = c0/9
			paths.append(1)
		else:
			c0 = s2+8
			paths.append(2)
		if c0 >= 1:
			s2 = s2*x
			c0 = c0*c0
			c0 = 9*c0
			paths.append(3)
		else:
			x = x-5
			c0 = 1*c0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		s2 = c0**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))