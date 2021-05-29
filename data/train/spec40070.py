import numpy as np 

def function(x):

	h7 = x
	h1 = x
	paths = []
	try:
		if x >= 7:
			h7 = h7+x
			x = x+7
			paths.append(1)
		else:
			h1 = 2/4
			paths.append(2)
		if h7 < 4:
			h7 = h7/4
			paths.append(3)
		else:
			h7 = 2*h7
			h7 = 4+h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))