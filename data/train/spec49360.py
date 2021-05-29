import numpy as np 

def function(x):

	t0 = 6
	h0 = 2
	paths = []
	try:
		if h0 > 7:
			x = 1*x
			x = t0-3
			paths.append(1)
		else:
			t0 = t0*x
			h0 = 7+h0
			paths.append(2)
		if x < 9:
			x = 2/x
			paths.append(3)
		else:
			h0 = 0+9
			x = x+h0
			h0 = x-x
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