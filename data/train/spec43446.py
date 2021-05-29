import numpy as np 

def function(x):

	d0 = 2
	w9 = x
	paths = []
	try:
		if d0 >= 1:
			d0 = d0-7
			paths.append(1)
		else:
			w9 = 9*w9
			d0 = w9/d0
			w9 = 5*w9
			paths.append(2)
		if x >= 9:
			x = 0+d0
			paths.append(3)
		else:
			w9 = 3-w9
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		w9 = d0**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))