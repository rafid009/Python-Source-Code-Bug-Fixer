import numpy as np 

def function(x):

	d1 = 6
	h6 = 7
	paths = []
	try:
		if h6 < 5:
			h6 = d1/9
			paths.append(1)
		else:
			x = x-9
			x = 6-x
			x = 9*x
			paths.append(2)
		if x <= 6:
			d1 = h6/6
			d1 = 5/d1
			x = 2/x
			paths.append(3)
		else:
			h6 = h6-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))