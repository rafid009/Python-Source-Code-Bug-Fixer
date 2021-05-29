import numpy as np 

def function(x):

	h0 = x
	s1 = 2
	paths = []
	try:
		if h0 > 5:
			h0 = 1-h0
			s1 = s1+8
			paths.append(1)
		else:
			x = 0/x
			h0 = x/5
			paths.append(2)
		if s1 < 2:
			s1 = 2*h0
			paths.append(3)
		else:
			x = h0-5
			x = x*4
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h0 = h0**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))