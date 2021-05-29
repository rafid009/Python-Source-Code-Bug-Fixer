import numpy as np 

def function(x):

	w1 = 8
	d0 = 8
	paths = []
	try:
		if d0 >= 0:
			x = 3/x
			paths.append(1)
		else:
			w1 = 9*w1
			x = 6/x
			paths.append(2)
		if w1 >= 0:
			d0 = 5-5
			w1 = w1+4
			x = x+d0
			paths.append(3)
		else:
			d0 = 9*d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))