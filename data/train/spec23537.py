import numpy as np 

def function(x):

	k0 = 1
	x9 = 8
	x = 2
	paths = []
	try:
		if x9 >= 9:
			x9 = x9/5
			paths.append(1)
		else:
			k0 = k0-x9
			x = x+5
			paths.append(2)
		if x9 >= 6:
			x9 = 4-x
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x9 = k0**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))