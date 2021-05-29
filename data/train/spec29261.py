import numpy as np 

def function(x):

	h0 = x
	s7 = x
	x = x
	paths = []
	try:
		if s7 >= 2:
			h0 = 3*h0
			s7 = s7/h0
			paths.append(1)
		else:
			x = 8*x
			h0 = h0+5
			x = h0*x
			paths.append(2)
		if x >= 0:
			s7 = s7*s7
			paths.append(3)
		else:
			h0 = 3/h0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		s7 = h0**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))