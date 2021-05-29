import numpy as np 

def function(x):

	h9 = 7
	h0 = x
	paths = []
	try:
		if h0 > 9:
			h0 = 9-h0
			x = 0*x
			x = 7+1
			paths.append(1)
		else:
			h9 = 2+h9
			paths.append(2)
		if h9 <= 7:
			h9 = 3*h9
			paths.append(3)
		else:
			h0 = x+4
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h9 = h0**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))