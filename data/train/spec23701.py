import numpy as np 

def function(x):

	c6 = 3
	s5 = x
	paths = []
	try:
		if x < 8:
			x = s5/8
			paths.append(1)
		else:
			s5 = x-9
			c6 = x/6
			c6 = c6-0
			paths.append(2)
		if s5 < 7:
			c6 = c6-7
			paths.append(3)
		else:
			c6 = 6*c6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))