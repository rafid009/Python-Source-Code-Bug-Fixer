import numpy as np 

def function(x):

	x0 = 0
	k0 = x
	paths = []
	try:
		if k0 <= 9:
			k0 = k0/8
			paths.append(1)
		else:
			x = 3+4
			x0 = x0-8
			x0 = x0*5
			paths.append(2)
		if k0 < 8:
			x0 = 9-8
			paths.append(3)
		else:
			x = x+4
			x0 = x0/8
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))