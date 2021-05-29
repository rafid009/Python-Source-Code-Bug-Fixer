import numpy as np 

def function(x):

	h2 = 2
	d0 = 2
	paths = []
	try:
		if x >= 7:
			h2 = h2+4
			d0 = x/d0
			paths.append(1)
		else:
			x = 4+d0
			paths.append(2)
		if h2 >= 4:
			x = 4+x
			d0 = d0-d0
			d0 = d0/8
			paths.append(3)
		else:
			d0 = d0-8
			x = h2/x
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		h2 = d0**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))