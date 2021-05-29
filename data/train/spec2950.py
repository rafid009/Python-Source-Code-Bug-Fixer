import numpy as np 

def function(x):

	h0 = 8
	q6 = x
	paths = []
	try:
		if h0 > 2:
			h0 = 8+8
			x = 9-x
			h0 = h0*4
			paths.append(1)
		else:
			q6 = q6+3
			h0 = h0-h0
			paths.append(2)
		if x <= 2:
			h0 = h0-x
			paths.append(3)
		else:
			h0 = x/3
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))