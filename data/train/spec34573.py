import numpy as np 

def function(x):

	j0 = x
	x8 = x
	x = 5
	paths = []
	try:
		if x8 < 4:
			x = 6+x
			x = x-2
			paths.append(1)
		else:
			j0 = 9-j0
			j0 = j0*x8
			x = 3/x
			paths.append(2)
		if x8 < 1:
			x = j0+7
			paths.append(3)
		else:
			x8 = x+j0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))