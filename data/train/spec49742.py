import numpy as np 

def function(x):

	r3 = 4
	k0 = 0
	paths = []
	try:
		if x < 6:
			r3 = 6/r3
			r3 = 1-4
			paths.append(1)
		else:
			r3 = 4*r3
			k0 = k0/9
			k0 = k0*k0
			paths.append(2)
		if k0 >= 6:
			k0 = 4-4
			paths.append(3)
		else:
			k0 = k0-2
			r3 = 0+x
			k0 = 7/k0
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