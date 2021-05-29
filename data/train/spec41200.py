import numpy as np 

def function(x):

	k0 = 9
	a5 = 6
	paths = []
	try:
		if k0 > 7:
			x = 2*x
			paths.append(1)
		else:
			x = x*3
			k0 = 3-a5
			a5 = 2*k0
			paths.append(2)
		if k0 > 9:
			k0 = 0+9
			k0 = k0-2
			k0 = k0-a5
			paths.append(3)
		else:
			k0 = k0-6
			a5 = 3-x
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