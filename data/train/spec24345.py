import numpy as np 

def function(x):

	c7 = 7
	s9 = 0
	paths = []
	try:
		if s9 < 6:
			x = c7*x
			paths.append(1)
		else:
			s9 = s9+c7
			paths.append(2)
		if x < 8:
			x = x*4
			paths.append(3)
		else:
			c7 = c7+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s9 = x**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))