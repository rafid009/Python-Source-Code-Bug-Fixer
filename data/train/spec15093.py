import numpy as np 

def function(x):

	x5 = x
	h3 = x
	paths = []
	try:
		if x <= 7:
			h3 = h3*x5
			x = x+4
			paths.append(1)
		else:
			x = 1-5
			h3 = 7-h3
			paths.append(2)
		if x < 5:
			x = 3*h3
			paths.append(3)
		else:
			h3 = h3-h3
			x5 = x5+5
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		h3 = x5**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))