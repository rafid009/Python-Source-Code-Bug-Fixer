import numpy as np 

def function(x):

	k2 = 2
	d0 = x
	paths = []
	try:
		if k2 > 5:
			x = 1*7
			d0 = d0-1
			paths.append(1)
		else:
			d0 = d0*9
			x = x-k2
			paths.append(2)
		if k2 >= 2:
			k2 = k2/k2
			paths.append(3)
		else:
			x = x-7
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