import numpy as np 

def function(x):

	w3 = 6
	k0 = x
	paths = []
	try:
		if w3 < 4:
			w3 = w3-k0
			w3 = w3-k0
			w3 = x-6
			paths.append(1)
		else:
			x = x-5
			k0 = k0-w3
			paths.append(2)
		if k0 > 4:
			k0 = 1*k0
			w3 = w3/k0
			x = 8-8
			paths.append(3)
		else:
			w3 = w3-0
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