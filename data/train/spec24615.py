import numpy as np 

def function(x):

	e7 = x
	n0 = x
	paths = []
	try:
		if x >= 6:
			e7 = e7-e7
			x = 3-2
			e7 = 1+3
			paths.append(1)
		else:
			n0 = 6/2
			e7 = e7/2
			paths.append(2)
		if e7 < 4:
			x = x/9
			e7 = n0-1
			paths.append(3)
		else:
			n0 = n0*x
			n0 = 2/1
			x = n0-n0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))