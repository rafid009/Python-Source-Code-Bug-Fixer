import numpy as np 

def function(x):

	q4 = x
	h0 = x
	x = 9
	paths = []
	try:
		if x >= 1:
			q4 = q4/2
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if q4 <= 8:
			h0 = 1-q4
			x = h0/x
			h0 = h0-4
			paths.append(3)
		else:
			x = x/5
			q4 = 1/q4
			x = h0-x
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		h0 = q4**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))