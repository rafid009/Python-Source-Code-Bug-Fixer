import numpy as np 

def function(x):

	h7 = 6
	d2 = 6
	paths = []
	try:
		if d2 > 7:
			h7 = 6/h7
			d2 = x*6
			paths.append(1)
		else:
			h7 = 6/h7
			paths.append(2)
		if h7 < 2:
			d2 = 2/7
			paths.append(3)
		else:
			h7 = d2*h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))