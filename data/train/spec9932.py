import numpy as np 

def function(x):

	h1 = x
	s8 = 2
	paths = []
	try:
		if h1 > 4:
			s8 = 7/x
			h1 = h1*2
			paths.append(1)
		else:
			x = x+5
			h1 = s8*x
			x = 1-4
			paths.append(2)
		if x >= 8:
			h1 = x/6
			h1 = h1/s8
			paths.append(3)
		else:
			s8 = x*9
			x = h1-x
			s8 = x-s8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))