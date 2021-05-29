import numpy as np 

def function(x):

	a0 = x
	x9 = 1
	paths = []
	try:
		if x9 >= 5:
			x9 = x9+a0
			a0 = a0-3
			x9 = x9-6
			paths.append(1)
		else:
			x9 = x9/a0
			paths.append(2)
		if a0 < 3:
			a0 = 4-2
			paths.append(3)
		else:
			x = x+1
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))