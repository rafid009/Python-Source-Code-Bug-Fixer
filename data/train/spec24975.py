import numpy as np 

def function(x):

	n0 = x
	v9 = 3
	paths = []
	try:
		if x >= 6:
			n0 = 5-n0
			n0 = n0+6
			paths.append(1)
		else:
			x = n0-4
			paths.append(2)
		if x < 9:
			n0 = v9+1
			paths.append(3)
		else:
			v9 = 0-v9
			n0 = n0+3
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		v9 = n0**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))