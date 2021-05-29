import numpy as np 

def function(x):

	n0 = x
	a5 = 6
	paths = []
	try:
		if a5 <= 4:
			n0 = 4/6
			n0 = n0+9
			n0 = n0*n0
			paths.append(1)
		else:
			n0 = 1-8
			paths.append(2)
		if n0 < 3:
			a5 = x-a5
			paths.append(3)
		else:
			a5 = 3-a5
			x = 9-x
			x = 1/x
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