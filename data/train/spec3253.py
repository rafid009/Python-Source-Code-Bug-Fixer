import numpy as np 

def function(x):

	k3 = 8
	e4 = 2
	paths = []
	try:
		if e4 >= 3:
			k3 = k3/4
			paths.append(1)
		else:
			x = x+6
			k3 = k3/6
			e4 = 9+e4
			paths.append(2)
		if e4 >= 0:
			k3 = k3*4
			paths.append(3)
		else:
			k3 = k3/3
			k3 = k3*1
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