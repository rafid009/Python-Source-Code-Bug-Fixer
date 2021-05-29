import numpy as np 

def function(x):

	y8 = x
	n0 = 8
	x = 3
	paths = []
	try:
		if y8 <= 5:
			y8 = y8-8
			x = 7-n0
			x = x*y8
			paths.append(1)
		else:
			y8 = 0*y8
			n0 = n0*n0
			paths.append(2)
		if y8 >= 0:
			x = n0/x
			paths.append(3)
		else:
			n0 = n0+n0
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))