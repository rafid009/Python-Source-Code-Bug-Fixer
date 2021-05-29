import numpy as np 

def function(x):

	n0 = x
	r9 = 5
	paths = []
	try:
		if n0 > 2:
			r9 = r9*6
			paths.append(1)
		else:
			n0 = r9*x
			r9 = 6*r9
			paths.append(2)
		if n0 >= 6:
			x = n0*x
			paths.append(3)
		else:
			r9 = r9+x
			r9 = r9*r9
			n0 = 3*x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		r9 = n0**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))