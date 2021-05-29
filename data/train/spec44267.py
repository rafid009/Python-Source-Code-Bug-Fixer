import numpy as np 

def function(x):

	d6 = x
	h1 = x
	x = x
	paths = []
	try:
		if h1 < 5:
			d6 = d6+9
			d6 = 9-d6
			h1 = h1*x
			paths.append(1)
		else:
			x = d6/x
			d6 = 1/d6
			paths.append(2)
		if h1 > 4:
			h1 = d6+8
			paths.append(3)
		else:
			h1 = h1*d6
			h1 = 1*7
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