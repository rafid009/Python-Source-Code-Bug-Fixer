import numpy as np 

def function(x):

	a0 = 4
	k2 = 7
	paths = []
	try:
		if x >= 5:
			x = x-9
			x = 9*a0
			x = 3/x
			paths.append(1)
		else:
			a0 = 1*k2
			a0 = 5/k2
			paths.append(2)
		if a0 >= 8:
			x = 3/k2
			x = 9*5
			k2 = a0/k2
			paths.append(3)
		else:
			k2 = 9*1
			a0 = 7-2
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