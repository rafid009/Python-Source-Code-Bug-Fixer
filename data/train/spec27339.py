import numpy as np 

def function(x):

	k3 = x
	x9 = 9
	paths = []
	try:
		if x9 > 6:
			x9 = x9/2
			x = x+x
			paths.append(1)
		else:
			x = x9/k3
			x9 = 1+x9
			paths.append(2)
		if x9 < 6:
			x = 7-x
			k3 = x9+x9
			k3 = k3-3
			paths.append(3)
		else:
			x9 = x9/x
			x = 0/6
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