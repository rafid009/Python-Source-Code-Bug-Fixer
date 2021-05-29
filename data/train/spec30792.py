import numpy as np 

def function(x):

	k0 = x
	paths = []
	try:
		if x >= 4:
			k0 = k0-4
			paths.append(1)
		else:
			x = k0-k0
			paths.append(2)
		if k0 < 9:
			k0 = 4-5
			k0 = k0-3
			paths.append(3)
		else:
			x = 6+3
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))