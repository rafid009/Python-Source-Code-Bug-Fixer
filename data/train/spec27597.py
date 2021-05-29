import numpy as np 

def function(x):

	k3 = x
	a6 = x
	x = x
	paths = []
	try:
		if k3 >= 9:
			k3 = 3*k3
			a6 = a6-0
			x = k3-8
			paths.append(1)
		else:
			k3 = k3*a6
			paths.append(2)
		if x >= 2:
			a6 = a6/a6
			x = x-5
			k3 = k3+5
			paths.append(3)
		else:
			k3 = k3-2
			k3 = k3*4
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