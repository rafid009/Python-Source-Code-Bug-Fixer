import numpy as np 

def function(x):

	r3 = 1
	k0 = 8
	paths = []
	try:
		if k0 < 7:
			r3 = r3*r3
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if x >= 7:
			k0 = k0-6
			k0 = 6-k0
			paths.append(3)
		else:
			x = x-6
			k0 = k0*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))