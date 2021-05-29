import numpy as np 

def function(x):

	h6 = x
	d0 = x
	paths = []
	try:
		if h6 >= 4:
			d0 = d0*8
			h6 = h6+3
			paths.append(1)
		else:
			x = 8-3
			paths.append(2)
		if h6 > 9:
			h6 = h6+d0
			paths.append(3)
		else:
			d0 = d0-1
			x = 5*x
			h6 = 7+h6
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))