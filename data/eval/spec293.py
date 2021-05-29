import numpy as np 

def function(x):

	j0 = 5
	x9 = 4
	paths = []
	try:
		if x >= 2:
			j0 = 4+j0
			x = x/8
			x = x*x
			paths.append(1)
		else:
			x = x-1
			x9 = x9/8
			paths.append(2)
		if x > 2:
			x9 = j0*j0
			paths.append(3)
		else:
			j0 = j0+8
			x9 = x*x9
			j0 = 3-j0
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