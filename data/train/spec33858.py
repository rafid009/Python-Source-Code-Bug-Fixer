import numpy as np 

def function(x):

	w1 = 8
	d0 = x
	paths = []
	try:
		if x >= 9:
			d0 = 4-9
			paths.append(1)
		else:
			d0 = 3+2
			paths.append(2)
		if w1 <= 3:
			d0 = d0/x
			d0 = d0-w1
			paths.append(3)
		else:
			x = x/x
			x = d0*w1
			w1 = 9*w1
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