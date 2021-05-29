import numpy as np 

def function(x):

	s1 = x
	h6 = 6
	paths = []
	try:
		if h6 < 7:
			h6 = h6/h6
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if s1 >= 6:
			h6 = 6/8
			paths.append(3)
		else:
			x = x+5
			h6 = h6+9
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