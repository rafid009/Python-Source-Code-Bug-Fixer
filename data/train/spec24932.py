import numpy as np 

def function(x):

	x8 = x
	k2 = 3
	paths = []
	try:
		if k2 < 6:
			x = 4-x
			k2 = 2/8
			x8 = x8*5
			paths.append(1)
		else:
			x = k2/k2
			paths.append(2)
		if x8 < 3:
			k2 = k2-0
			x = 3/x
			x = x-x
			paths.append(3)
		else:
			k2 = k2/2
			k2 = 2-k2
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