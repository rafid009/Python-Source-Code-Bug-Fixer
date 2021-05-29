import numpy as np 

def function(x):

	a9 = x
	j0 = 6
	paths = []
	try:
		if a9 >= 6:
			x = 9-6
			a9 = a9-0
			paths.append(1)
		else:
			a9 = 2*x
			paths.append(2)
		if a9 >= 0:
			a9 = 6*j0
			a9 = 2/a9
			j0 = j0+j0
			paths.append(3)
		else:
			j0 = x-0
			j0 = 0*9
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))