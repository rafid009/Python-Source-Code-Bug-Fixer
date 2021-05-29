import numpy as np 

def function(x):

	k9 = 6
	h0 = 4
	paths = []
	try:
		if x < 0:
			h0 = h0-h0
			h0 = 7+x
			x = 9*x
			paths.append(1)
		else:
			k9 = x+k9
			paths.append(2)
		if h0 >= 3:
			x = h0-0
			paths.append(3)
		else:
			k9 = k9*5
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