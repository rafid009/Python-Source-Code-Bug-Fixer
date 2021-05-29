import numpy as np 

def function(x):

	d7 = 4
	h7 = 1
	paths = []
	try:
		if h7 >= 5:
			d7 = 6-d7
			h7 = d7*h7
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if d7 < 8:
			d7 = h7*d7
			d7 = 4*x
			x = x-h7
			paths.append(3)
		else:
			d7 = 6-8
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