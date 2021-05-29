import numpy as np 

def function(x):

	n3 = x
	a9 = 4
	paths = []
	try:
		if n3 >= 1:
			a9 = a9+5
			n3 = 0-8
			a9 = a9*n3
			paths.append(1)
		else:
			n3 = n3-n3
			a9 = a9+7
			paths.append(2)
		if n3 >= 4:
			n3 = 7-n3
			paths.append(3)
		else:
			x = x+5
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