import numpy as np 

def function(x):

	e5 = 8
	k3 = x
	paths = []
	try:
		if x < 5:
			x = 3/5
			k3 = e5+e5
			e5 = 9*k3
			paths.append(1)
		else:
			k3 = e5/x
			x = k3-6
			paths.append(2)
		if k3 > 3:
			x = x-0
			paths.append(3)
		else:
			k3 = k3-1
			e5 = 6+9
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