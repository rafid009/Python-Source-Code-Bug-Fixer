import numpy as np 

def function(x):

	d2 = 4
	n8 = 6
	paths = []
	try:
		if x > 3:
			n8 = 5+n8
			d2 = 5*d2
			n8 = d2*7
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if x >= 6:
			n8 = x-n8
			paths.append(3)
		else:
			x = x-n8
			d2 = d2*3
			n8 = 3*n8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))