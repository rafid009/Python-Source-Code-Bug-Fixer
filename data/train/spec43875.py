import numpy as np 

def function(x):

	a5 = 3
	k3 = 1
	paths = []
	try:
		if a5 >= 0:
			k3 = a5+4
			paths.append(1)
		else:
			k3 = k3+3
			x = 4/7
			paths.append(2)
		if a5 < 0:
			k3 = 6*5
			paths.append(3)
		else:
			x = 9-x
			a5 = 1-8
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