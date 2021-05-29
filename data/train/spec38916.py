import numpy as np 

def function(x):

	d1 = 6
	k0 = 9
	paths = []
	try:
		if x <= 6:
			k0 = x-8
			x = k0-x
			d1 = d1+4
			paths.append(1)
		else:
			k0 = 9*d1
			x = 3+3
			x = k0+x
			paths.append(2)
		if x > 1:
			x = x+2
			d1 = k0+3
			paths.append(3)
		else:
			k0 = 9*d1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))