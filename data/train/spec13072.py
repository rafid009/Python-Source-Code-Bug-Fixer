import numpy as np 

def function(x):

	n0 = 9
	w4 = 3
	paths = []
	try:
		if w4 <= 8:
			n0 = x+n0
			w4 = w4-x
			paths.append(1)
		else:
			n0 = x-5
			n0 = 5*n0
			x = 4+9
			paths.append(2)
		if x <= 8:
			w4 = w4*5
			n0 = n0*3
			paths.append(3)
		else:
			n0 = x*n0
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))