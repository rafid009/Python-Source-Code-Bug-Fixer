import numpy as np 

def function(x):

	h3 = 7
	h8 = 6
	paths = []
	try:
		if h8 >= 8:
			h3 = h3*0
			paths.append(1)
		else:
			x = x+5
			h3 = x/h3
			x = h3-h8
			paths.append(2)
		if h8 > 8:
			x = x-6
			x = x-x
			paths.append(3)
		else:
			h3 = 7+h3
			h3 = h3-h3
			h8 = h3*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))