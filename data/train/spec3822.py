import numpy as np 

def function(x):

	n0 = 6
	v9 = 8
	paths = []
	try:
		if v9 >= 6:
			v9 = v9/v9
			n0 = x-n0
			v9 = v9+n0
			paths.append(1)
		else:
			x = x-n0
			paths.append(2)
		if n0 >= 1:
			n0 = 0/v9
			v9 = 5-v9
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))