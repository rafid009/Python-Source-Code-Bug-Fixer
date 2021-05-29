import numpy as np 

def function(x):

	d2 = 3
	h3 = 8
	paths = []
	try:
		if d2 > 8:
			x = x*d2
			d2 = d2/2
			paths.append(1)
		else:
			d2 = 9/d2
			h3 = h3+h3
			paths.append(2)
		if h3 < 1:
			x = x*d2
			x = x/9
			paths.append(3)
		else:
			x = 9-h3
			h3 = 1-x
			d2 = d2/h3
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