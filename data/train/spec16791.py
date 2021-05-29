import numpy as np 

def function(x):

	h0 = 5
	l6 = x
	paths = []
	try:
		if x < 0:
			h0 = 6*x
			paths.append(1)
		else:
			h0 = h0-8
			x = 9/x
			x = x-3
			paths.append(2)
		if h0 < 4:
			h0 = h0+h0
			h0 = h0*9
			paths.append(3)
		else:
			x = h0+l6
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