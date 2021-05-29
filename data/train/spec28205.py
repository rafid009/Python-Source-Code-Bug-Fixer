import numpy as np 

def function(x):

	k0 = 2
	a6 = 3
	paths = []
	try:
		if k0 > 1:
			k0 = 8*9
			a6 = a6*8
			paths.append(1)
		else:
			a6 = a6-1
			x = 9-x
			x = x*x
			paths.append(2)
		if a6 >= 0:
			k0 = k0*4
			paths.append(3)
		else:
			x = 0*1
			k0 = k0-4
			x = 1+8
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