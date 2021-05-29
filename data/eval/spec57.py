import numpy as np 

def function(x):

	k4 = x
	h0 = 2
	paths = []
	try:
		if k4 <= 9:
			k4 = k4-1
			k4 = 3/k4
			paths.append(1)
		else:
			h0 = 8-k4
			paths.append(2)
		if h0 >= 6:
			x = 3+x
			x = 0-x
			paths.append(3)
		else:
			k4 = x+k4
			h0 = h0+4
			x = 2/x
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