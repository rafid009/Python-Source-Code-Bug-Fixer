import numpy as np 

def function(x):

	w8 = 4
	d0 = 7
	paths = []
	try:
		if x >= 5:
			w8 = w8-x
			d0 = w8*8
			d0 = d0/d0
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if x > 1:
			d0 = w8/6
			paths.append(3)
		else:
			x = x-5
			w8 = 1-w8
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