import numpy as np 

def function(x):

	h4 = 9
	d0 = x
	paths = []
	try:
		if d0 > 1:
			h4 = h4/9
			h4 = h4*x
			h4 = 1*8
			paths.append(1)
		else:
			d0 = 6-d0
			d0 = d0-9
			x = h4+x
			paths.append(2)
		if d0 > 6:
			h4 = h4+h4
			h4 = h4-7
			h4 = h4*d0
			paths.append(3)
		else:
			h4 = 9-h4
			h4 = d0*7
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