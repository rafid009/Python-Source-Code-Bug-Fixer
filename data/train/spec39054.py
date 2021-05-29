import numpy as np 

def function(x):

	k4 = x
	n0 = 9
	paths = []
	try:
		if k4 > 6:
			n0 = n0+4
			n0 = 5/x
			paths.append(1)
		else:
			n0 = n0/1
			k4 = 6-k4
			k4 = x-0
			paths.append(2)
		if k4 < 2:
			k4 = k4/x
			paths.append(3)
		else:
			k4 = k4*x
			k4 = n0+n0
			x = x*7
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