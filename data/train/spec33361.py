import numpy as np 

def function(x):

	s7 = 8
	h5 = x
	paths = []
	try:
		if x >= 4:
			s7 = 4*s7
			paths.append(1)
		else:
			h5 = s7*h5
			x = x/s7
			paths.append(2)
		if x > 4:
			x = h5/h5
			paths.append(3)
		else:
			h5 = h5-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))