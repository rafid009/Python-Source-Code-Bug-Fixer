import numpy as np 

def function(x):

	k3 = 3
	x5 = x
	paths = []
	try:
		if x >= 3:
			x = 4/x
			x5 = 7-9
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x > 9:
			k3 = k3*k3
			k3 = k3/6
			paths.append(3)
		else:
			x5 = 7/x5
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))