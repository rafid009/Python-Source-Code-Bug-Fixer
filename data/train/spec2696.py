import numpy as np 

def function(x):

	i4 = x
	n0 = 5
	paths = []
	try:
		if i4 < 5:
			x = x*6
			x = 2/x
			paths.append(1)
		else:
			n0 = n0-x
			paths.append(2)
		if n0 < 4:
			n0 = n0*x
			i4 = 3*i4
			i4 = i4*4
			paths.append(3)
		else:
			n0 = x*n0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))