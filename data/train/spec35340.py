import numpy as np 

def function(x):

	s6 = x
	h2 = x
	x = 2
	paths = []
	try:
		if h2 <= 1:
			x = s6*6
			paths.append(1)
		else:
			x = 1/x
			s6 = s6/8
			paths.append(2)
		if s6 <= 3:
			h2 = h2-2
			paths.append(3)
		else:
			x = 7/6
			s6 = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))