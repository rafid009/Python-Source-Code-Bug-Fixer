import numpy as np 

def function(x):

	n0 = x
	v7 = 1
	x = 1
	paths = []
	try:
		if n0 >= 8:
			n0 = n0*n0
			n0 = 2-1
			v7 = 7+v7
			paths.append(1)
		else:
			v7 = v7-3
			n0 = n0-x
			paths.append(2)
		if n0 <= 2:
			x = 2+x
			paths.append(3)
		else:
			x = x+1
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