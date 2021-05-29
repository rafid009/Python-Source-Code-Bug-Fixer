import numpy as np 

def function(x):

	k3 = x
	a6 = x
	paths = []
	try:
		if x > 9:
			x = 6-x
			paths.append(1)
		else:
			x = 4*a6
			x = a6*6
			k3 = k3*2
			paths.append(2)
		if x >= 5:
			x = 3/a6
			k3 = 4+4
			paths.append(3)
		else:
			a6 = a6+4
			x = 1-x
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