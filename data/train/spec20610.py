import numpy as np 

def function(x):

	d4 = 4
	h4 = 4
	paths = []
	try:
		if h4 >= 1:
			h4 = h4-2
			paths.append(1)
		else:
			x = 5*8
			paths.append(2)
		if x >= 8:
			x = x*2
			d4 = d4-d4
			d4 = d4-d4
			paths.append(3)
		else:
			x = x*d4
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))