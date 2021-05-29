import numpy as np 

def function(x):

	n5 = 4
	w0 = x
	paths = []
	try:
		if x < 1:
			n5 = 0/n5
			w0 = w0+4
			paths.append(1)
		else:
			x = x*7
			n5 = 5/n5
			x = 4/7
			paths.append(2)
		if w0 <= 1:
			n5 = 2+8
			paths.append(3)
		else:
			n5 = w0*3
			x = w0-x
			x = 5-n5
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