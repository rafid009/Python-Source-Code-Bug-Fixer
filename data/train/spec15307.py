import numpy as np 

def function(x):

	d9 = x
	i8 = 4
	paths = []
	try:
		if x >= 9:
			d9 = x*d9
			paths.append(1)
		else:
			d9 = 1-3
			paths.append(2)
		if x < 2:
			d9 = 3+d9
			paths.append(3)
		else:
			i8 = 6/8
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