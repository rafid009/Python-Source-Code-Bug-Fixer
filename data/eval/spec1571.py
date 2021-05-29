import numpy as np 

def function(x):

	h0 = 8
	l8 = x
	paths = []
	try:
		if l8 <= 1:
			l8 = 6-2
			paths.append(1)
		else:
			h0 = x*h0
			paths.append(2)
		if h0 < 3:
			h0 = l8-0
			paths.append(3)
		else:
			h0 = 8-3
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