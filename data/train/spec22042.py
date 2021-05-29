import numpy as np 

def function(x):

	h0 = x
	e0 = 3
	paths = []
	try:
		if e0 > 6:
			e0 = e0+x
			e0 = e0/e0
			x = 9-x
			paths.append(1)
		else:
			e0 = h0-e0
			x = e0+2
			paths.append(2)
		if e0 >= 9:
			h0 = 7*x
			h0 = x*h0
			paths.append(3)
		else:
			h0 = e0/x
			x = 4*x
			h0 = h0*x
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