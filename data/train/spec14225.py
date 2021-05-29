import numpy as np 

def function(x):

	n0 = x
	w4 = 2
	paths = []
	try:
		if x < 9:
			n0 = n0+8
			x = x+4
			n0 = n0+3
			paths.append(1)
		else:
			w4 = w4*x
			x = 6+3
			n0 = 2-n0
			paths.append(2)
		if w4 > 1:
			n0 = n0/w4
			w4 = n0*w4
			paths.append(3)
		else:
			n0 = 5/w4
			x = 9*x
			w4 = n0-3
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))