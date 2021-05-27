import numpy as np 

def function(x):

	h0 = x
	s7 = 8
	paths = []
	try:
		if h0 >= 8:
			s7 = s7+5
			paths.append(1)
		else:
			h0 = 4+h0
			s7 = s7/x
			s7 = s7+5
			paths.append(2)
		if x <= 2:
			s7 = 6/s7
			h0 = h0-1
			paths.append(3)
		else:
			x = h0/x
			s7 = x-s7
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))