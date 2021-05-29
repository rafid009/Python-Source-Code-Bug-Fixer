import numpy as np 

def function(x):

	k0 = 7
	r3 = 7
	paths = []
	try:
		if r3 >= 4:
			k0 = 2/k0
			paths.append(1)
		else:
			x = k0-k0
			paths.append(2)
		if k0 >= 4:
			k0 = 3+3
			r3 = 7+k0
			r3 = r3+3
			paths.append(3)
		else:
			k0 = 1/5
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