import numpy as np 

def function(x):

	a3 = x
	f1 = 3
	paths = []
	try:
		if a3 > 8:
			a3 = a3*9
			f1 = 1/x
			x = x+a3
			paths.append(1)
		else:
			x = 1/a3
			paths.append(2)
		if a3 >= 2:
			f1 = f1/6
			paths.append(3)
		else:
			a3 = a3+8
			x = x-f1
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