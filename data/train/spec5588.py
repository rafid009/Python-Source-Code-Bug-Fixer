import numpy as np 

def function(x):

	x4 = 3
	a3 = x
	paths = []
	try:
		if a3 >= 6:
			x4 = a3-x4
			paths.append(1)
		else:
			a3 = a3+a3
			paths.append(2)
		if x4 >= 6:
			a3 = a3/3
			paths.append(3)
		else:
			x = 6*x
			x = 0/x
			a3 = a3+a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))