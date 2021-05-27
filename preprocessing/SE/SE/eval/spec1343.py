import numpy as np 

def function(x):

	d5 = x
	w7 = x
	paths = []
	try:
		if d5 < 3:
			x = 2/x
			d5 = 7*d5
			w7 = 9-7
			paths.append(1)
		else:
			w7 = w7/4
			paths.append(2)
		if d5 < 6:
			w7 = w7+6
			d5 = x/x
			w7 = w7/d5
			paths.append(3)
		else:
			x = w7+d5
			w7 = x-7
			x = 8/x
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