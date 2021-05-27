import numpy as np 

def function(x):

	c0 = x
	s7 = x
	paths = []
	try:
		if x < 1:
			c0 = 3/c0
			paths.append(1)
		else:
			s7 = s7-2
			s7 = 9*0
			paths.append(2)
		if c0 > 4:
			x = c0+2
			s7 = 8+s7
			c0 = 7-c0
			paths.append(3)
		else:
			x = x+s7
			c0 = 0*x
			s7 = 1/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))