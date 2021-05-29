import numpy as np 

def function(x):

	h0 = x
	n4 = 5
	paths = []
	try:
		if x <= 6:
			n4 = n4+6
			paths.append(1)
		else:
			h0 = h0*n4
			paths.append(2)
		if n4 > 6:
			x = x*8
			x = x*1
			paths.append(3)
		else:
			x = 7/8
			n4 = 3-4
			h0 = 5*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))