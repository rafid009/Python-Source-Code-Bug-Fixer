import numpy as np 

def function(x):

	k0 = x
	e7 = 3
	paths = []
	try:
		if k0 < 3:
			e7 = 6-e7
			k0 = k0/k0
			paths.append(1)
		else:
			x = 9/2
			paths.append(2)
		if k0 <= 3:
			x = x+x
			paths.append(3)
		else:
			k0 = e7/k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))