import numpy as np 

def function(x):

	d8 = 1
	h0 = x
	paths = []
	try:
		if x >= 9:
			h0 = 5/h0
			x = 4/x
			paths.append(1)
		else:
			h0 = h0+h0
			paths.append(2)
		if d8 < 5:
			x = 5+x
			paths.append(3)
		else:
			d8 = 3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))