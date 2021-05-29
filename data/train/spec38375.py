import numpy as np 

def function(x):

	w7 = 7
	h3 = 3
	paths = []
	try:
		if h3 > 5:
			x = x/3
			h3 = w7*h3
			x = x+6
			paths.append(1)
		else:
			h3 = h3-x
			paths.append(2)
		if h3 < 6:
			w7 = w7+8
			w7 = 9*w7
			paths.append(3)
		else:
			h3 = w7*2
			h3 = h3-h3
			x = w7+w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))