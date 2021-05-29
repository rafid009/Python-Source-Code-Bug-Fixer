import numpy as np 

def function(x):

	d6 = 6
	h3 = x
	x = 5
	paths = []
	try:
		if h3 > 9:
			x = 1-x
			paths.append(1)
		else:
			h3 = d6*h3
			h3 = h3/h3
			h3 = d6/h3
			paths.append(2)
		if x < 8:
			x = d6-x
			h3 = 1*h3
			x = x-3
			paths.append(3)
		else:
			h3 = x/3
			x = x/x
			x = 1+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))