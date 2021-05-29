import numpy as np 

def function(x):

	v0 = 7
	h0 = x
	paths = []
	try:
		if h0 <= 1:
			x = h0/x
			paths.append(1)
		else:
			v0 = x+v0
			paths.append(2)
		if h0 <= 2:
			x = h0*x
			paths.append(3)
		else:
			v0 = x/3
			h0 = h0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))