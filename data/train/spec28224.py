import numpy as np 

def function(x):

	k0 = x
	x4 = x
	paths = []
	try:
		if x4 >= 8:
			k0 = k0-1
			x = 9*6
			paths.append(1)
		else:
			x4 = x4*3
			x = 9/x
			paths.append(2)
		if x4 <= 6:
			x = x+k0
			paths.append(3)
		else:
			x = x/x4
			x4 = 3+k0
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))