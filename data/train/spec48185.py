import numpy as np 

def function(x):

	x7 = 6
	k3 = 5
	paths = []
	try:
		if x7 >= 3:
			k3 = 8*k3
			x7 = x7+x
			paths.append(1)
		else:
			x7 = 3*x7
			paths.append(2)
		if x > 0:
			x = x-6
			paths.append(3)
		else:
			x = x/4
			x = x-k3
			x7 = x7-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))