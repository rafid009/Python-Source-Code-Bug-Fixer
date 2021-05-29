import numpy as np 

def function(x):

	h0 = x
	a4 = 2
	paths = []
	try:
		if h0 < 0:
			a4 = a4/a4
			x = h0+a4
			paths.append(1)
		else:
			h0 = x*h0
			x = 5-x
			a4 = 6-h0
			paths.append(2)
		if h0 <= 6:
			x = x/7
			paths.append(3)
		else:
			h0 = 5*h0
			a4 = a4*6
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		h0 = a4**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))