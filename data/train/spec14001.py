import numpy as np 

def function(x):

	d1 = 6
	h0 = 6
	paths = []
	try:
		if h0 <= 7:
			x = x-8
			h0 = 4*h0
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if d1 >= 1:
			d1 = h0+x
			d1 = d1*1
			paths.append(3)
		else:
			h0 = x-5
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