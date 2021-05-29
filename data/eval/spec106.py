import numpy as np 

def function(x):

	r2 = 3
	k0 = x
	paths = []
	try:
		if k0 > 4:
			r2 = 7*r2
			paths.append(1)
		else:
			k0 = k0/x
			paths.append(2)
		if r2 <= 8:
			r2 = k0-2
			paths.append(3)
		else:
			k0 = 5/5
			r2 = x/5
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