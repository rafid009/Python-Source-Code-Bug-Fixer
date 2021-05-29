import numpy as np 

def function(x):

	i8 = x
	x4 = 6
	paths = []
	try:
		if x >= 1:
			i8 = i8-4
			x = x*x
			x = x*8
			paths.append(1)
		else:
			x = x/x4
			paths.append(2)
		if i8 >= 1:
			x4 = 4/3
			x = x-x
			paths.append(3)
		else:
			i8 = 3-7
			x4 = x4/x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))