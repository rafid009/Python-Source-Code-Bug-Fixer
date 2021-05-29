import numpy as np 

def function(x):

	k0 = x
	q3 = 2
	paths = []
	try:
		if k0 <= 4:
			k0 = 7-k0
			paths.append(1)
		else:
			k0 = k0/2
			q3 = 2*q3
			paths.append(2)
		if q3 <= 1:
			k0 = k0-3
			paths.append(3)
		else:
			q3 = q3-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))