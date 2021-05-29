import numpy as np 

def function(x):

	y8 = x
	i9 = x
	paths = []
	try:
		if x <= 6:
			y8 = 3/y8
			i9 = 3/y8
			paths.append(1)
		else:
			i9 = i9/9
			y8 = 4*4
			y8 = y8*x
			paths.append(2)
		if x > 9:
			i9 = 6*8
			i9 = 4/x
			x = 4/x
			paths.append(3)
		else:
			y8 = x-y8
			i9 = i9-y8
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