import numpy as np 

def function(x):

	d7 = x
	h8 = x
	paths = []
	try:
		if h8 < 3:
			h8 = x*h8
			d7 = d7/9
			paths.append(1)
		else:
			x = h8*x
			d7 = 2-d7
			d7 = 3+d7
			paths.append(2)
		if d7 > 0:
			d7 = d7/9
			h8 = x*3
			x = x*x
			paths.append(3)
		else:
			d7 = 0*d7
			d7 = d7+d7
			h8 = h8/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))