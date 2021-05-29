import numpy as np 

def function(x):

	h0 = x
	p3 = 8
	paths = []
	try:
		if x > 6:
			h0 = 4/h0
			p3 = p3*4
			x = 0*6
			paths.append(1)
		else:
			h0 = h0+p3
			paths.append(2)
		if h0 > 6:
			h0 = p3-5
			paths.append(3)
		else:
			h0 = h0+5
			h0 = 1-h0
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