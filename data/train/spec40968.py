import numpy as np 

def function(x):

	a8 = x
	a9 = 4
	paths = []
	try:
		if a8 >= 8:
			a8 = a8*a8
			paths.append(1)
		else:
			a8 = 0-0
			paths.append(2)
		if a9 <= 2:
			a9 = a9+x
			a9 = a9-a8
			paths.append(3)
		else:
			a9 = 0-a8
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