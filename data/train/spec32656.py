import numpy as np 

def function(x):

	i7 = 8
	z0 = x
	paths = []
	try:
		if x <= 6:
			i7 = 1*z0
			x = 3*x
			paths.append(1)
		else:
			x = 3/z0
			paths.append(2)
		if z0 >= 0:
			x = x-3
			i7 = 5+8
			paths.append(3)
		else:
			x = x-4
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))