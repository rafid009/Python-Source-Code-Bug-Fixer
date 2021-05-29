import numpy as np 

def function(x):

	k3 = x
	e3 = 7
	paths = []
	try:
		if k3 > 8:
			e3 = 0*k3
			paths.append(1)
		else:
			e3 = 7-9
			k3 = k3/k3
			paths.append(2)
		if e3 < 6:
			k3 = k3+0
			x = 1/x
			paths.append(3)
		else:
			e3 = e3/x
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