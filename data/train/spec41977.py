import numpy as np 

def function(x):

	n0 = x
	i8 = x
	paths = []
	try:
		if n0 <= 6:
			n0 = n0*i8
			i8 = 0/i8
			paths.append(1)
		else:
			x = x-4
			x = 9*i8
			paths.append(2)
		if n0 <= 5:
			i8 = 4-0
			i8 = 9+i8
			paths.append(3)
		else:
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))