import numpy as np 

def function(x):

	k0 = x
	b5 = 5
	paths = []
	try:
		if k0 >= 2:
			x = x*k0
			b5 = 5*b5
			k0 = k0-x
			paths.append(1)
		else:
			b5 = b5+6
			paths.append(2)
		if x <= 2:
			x = x/5
			paths.append(3)
		else:
			k0 = k0/k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))