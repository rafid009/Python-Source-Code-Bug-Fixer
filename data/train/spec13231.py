import numpy as np 

def function(x):

	s9 = 3
	h0 = 9
	paths = []
	try:
		if s9 > 0:
			x = 5-6
			x = 3/4
			paths.append(1)
		else:
			h0 = 7*h0
			paths.append(2)
		if h0 > 5:
			h0 = 7-9
			s9 = s9-s9
			h0 = h0-s9
			paths.append(3)
		else:
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))