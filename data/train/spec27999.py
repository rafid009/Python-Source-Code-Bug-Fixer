import numpy as np 

def function(x):

	k0 = x
	k2 = x
	paths = []
	try:
		if k0 >= 8:
			k0 = k0-8
			x = k0/x
			paths.append(1)
		else:
			k0 = k2*5
			k0 = 9-7
			paths.append(2)
		if x > 9:
			k2 = 3/k2
			paths.append(3)
		else:
			k0 = 5*6
			k2 = k2-7
			k0 = k0+0
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))