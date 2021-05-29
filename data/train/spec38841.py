import numpy as np 

def function(x):

	x7 = x
	n0 = 8
	paths = []
	try:
		if x < 4:
			x7 = 5/x7
			n0 = 6+n0
			paths.append(1)
		else:
			x7 = x7*x7
			paths.append(2)
		if x > 4:
			x7 = x7*4
			x = 8-n0
			n0 = x*n0
			paths.append(3)
		else:
			n0 = 7-x7
			n0 = 0-n0
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		n0 = x7**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))