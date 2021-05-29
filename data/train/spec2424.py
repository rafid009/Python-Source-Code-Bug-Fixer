import numpy as np 

def function(x):

	h0 = 6
	n4 = 7
	paths = []
	try:
		if n4 <= 9:
			n4 = h0+x
			h0 = h0+x
			n4 = n4+2
			paths.append(1)
		else:
			x = n4-2
			n4 = 7*n4
			paths.append(2)
		if h0 > 0:
			n4 = n4-n4
			h0 = h0*x
			paths.append(3)
		else:
			h0 = 9*6
			x = 5-x
			h0 = n4*h0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		n4 = h0**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))