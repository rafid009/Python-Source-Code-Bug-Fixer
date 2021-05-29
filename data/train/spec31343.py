import numpy as np 

def function(x):

	a4 = 5
	x1 = 7
	paths = []
	try:
		if a4 > 0:
			x1 = x/x
			paths.append(1)
		else:
			a4 = a4+3
			a4 = x-7
			x = x/9
			paths.append(2)
		if a4 >= 9:
			x1 = 3*x1
			a4 = 1-a4
			x = x+x1
			paths.append(3)
		else:
			x = x1-3
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