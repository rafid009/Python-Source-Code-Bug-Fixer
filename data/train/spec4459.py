import numpy as np 

def function(x):

	a9 = 2
	d4 = 1
	paths = []
	try:
		if a9 >= 1:
			a9 = a9+d4
			paths.append(1)
		else:
			a9 = a9/8
			paths.append(2)
		if x >= 6:
			x = x-7
			paths.append(3)
		else:
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))