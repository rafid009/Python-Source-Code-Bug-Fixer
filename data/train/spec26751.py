import numpy as np 

def function(x):

	k3 = 8
	a4 = x
	paths = []
	try:
		if x >= 0:
			a4 = a4-3
			paths.append(1)
		else:
			k3 = 7*k3
			paths.append(2)
		if k3 >= 0:
			k3 = 0-9
			paths.append(3)
		else:
			a4 = a4-9
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