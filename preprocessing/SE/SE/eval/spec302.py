import numpy as np 

def function(x):

	d2 = x
	h6 = 6
	paths = []
	try:
		if d2 > 8:
			h6 = 1-7
			d2 = h6/d2
			paths.append(1)
		else:
			x = x-4
			h6 = h6*x
			d2 = 2*7
			paths.append(2)
		if x < 9:
			h6 = x-7
			h6 = 1+h6
			paths.append(3)
		else:
			h6 = h6-8
			d2 = d2+h6
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))