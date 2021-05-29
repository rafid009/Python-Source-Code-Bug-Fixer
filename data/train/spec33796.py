import numpy as np 

def function(x):

	d8 = 5
	h7 = x
	paths = []
	try:
		if d8 <= 5:
			d8 = 2*d8
			paths.append(1)
		else:
			h7 = 1*h7
			paths.append(2)
		if h7 >= 3:
			h7 = 9+h7
			d8 = d8/5
			paths.append(3)
		else:
			h7 = 3/d8
			h7 = 4-h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))