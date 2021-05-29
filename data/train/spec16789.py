import numpy as np 

def function(x):

	s4 = x
	h0 = x
	paths = []
	try:
		if h0 < 8:
			s4 = h0-s4
			s4 = 7+s4
			x = 5+h0
			paths.append(1)
		else:
			x = 9*s4
			h0 = h0*x
			paths.append(2)
		if h0 <= 8:
			x = x/1
			paths.append(3)
		else:
			h0 = 4*9
			x = x/6
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))