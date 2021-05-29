import numpy as np 

def function(x):

	d8 = 1
	w6 = 0
	paths = []
	try:
		if x > 9:
			x = 1+6
			w6 = 4-3
			d8 = 7*d8
			paths.append(1)
		else:
			d8 = d8+2
			paths.append(2)
		if w6 < 0:
			w6 = w6-w6
			paths.append(3)
		else:
			w6 = w6*7
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