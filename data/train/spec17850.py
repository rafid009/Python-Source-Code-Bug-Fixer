import numpy as np 

def function(x):

	k3 = 0
	q3 = 8
	paths = []
	try:
		if k3 < 1:
			k3 = k3-4
			k3 = 9-k3
			k3 = 3+2
			paths.append(1)
		else:
			k3 = k3-2
			paths.append(2)
		if k3 > 6:
			x = x/2
			k3 = k3*5
			paths.append(3)
		else:
			x = k3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k3 = x**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))