import numpy as np 

def function(x):

	h8 = 4
	d0 = x
	paths = []
	try:
		if x >= 1:
			h8 = d0/h8
			paths.append(1)
		else:
			d0 = 7*d0
			paths.append(2)
		if h8 < 8:
			x = x+h8
			d0 = d0*1
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))