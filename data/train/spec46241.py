import numpy as np 

def function(x):

	a8 = 2
	f1 = 6
	paths = []
	try:
		if x > 1:
			a8 = 3-a8
			a8 = a8*f1
			paths.append(1)
		else:
			a8 = f1-a8
			paths.append(2)
		if x > 9:
			a8 = 1-a8
			paths.append(3)
		else:
			a8 = 9+a8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))