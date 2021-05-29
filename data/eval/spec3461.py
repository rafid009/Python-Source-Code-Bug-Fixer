import numpy as np 

def function(x):

	i0 = 4
	x2 = x
	paths = []
	try:
		if x >= 1:
			i0 = i0+6
			paths.append(1)
		else:
			i0 = i0+6
			i0 = i0/x2
			x = x2+i0
			paths.append(2)
		if x <= 2:
			x2 = x2/x2
			paths.append(3)
		else:
			i0 = 8-2
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