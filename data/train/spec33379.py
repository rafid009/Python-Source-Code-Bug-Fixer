import numpy as np 

def function(x):

	k0 = x
	w9 = 7
	paths = []
	try:
		if x <= 9:
			x = x-6
			paths.append(1)
		else:
			w9 = w9-k0
			w9 = w9*w9
			paths.append(2)
		if k0 < 2:
			k0 = k0-3
			paths.append(3)
		else:
			x = x+k0
			x = x*x
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