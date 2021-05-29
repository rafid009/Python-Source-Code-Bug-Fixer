import numpy as np 

def function(x):

	x1 = x
	a6 = 5
	paths = []
	try:
		if x1 >= 5:
			a6 = 9-a6
			paths.append(1)
		else:
			x1 = a6-4
			x1 = x1*x1
			paths.append(2)
		if x1 > 3:
			x1 = x1*a6
			x1 = x1-x
			x = x+a6
			paths.append(3)
		else:
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))