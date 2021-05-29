import numpy as np 

def function(x):

	j0 = x
	o7 = 9
	paths = []
	try:
		if x <= 9:
			o7 = 6*3
			x = 8*x
			j0 = o7+4
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if x <= 9:
			j0 = 4/j0
			j0 = 9-o7
			o7 = o7*1
			paths.append(3)
		else:
			x = 3*x
			x = 3+2
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