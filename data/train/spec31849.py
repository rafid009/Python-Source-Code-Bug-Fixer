import numpy as np 

def function(x):

	h3 = x
	d1 = 5
	paths = []
	try:
		if h3 > 1:
			d1 = 8/8
			paths.append(1)
		else:
			h3 = h3+8
			h3 = 7-h3
			paths.append(2)
		if x <= 4:
			h3 = h3-0
			h3 = 3*8
			paths.append(3)
		else:
			d1 = d1+0
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