import numpy as np 

def function(x):

	i8 = x
	v1 = x
	paths = []
	try:
		if i8 >= 0:
			x = x*6
			v1 = 1-1
			paths.append(1)
		else:
			v1 = v1+0
			paths.append(2)
		if x <= 6:
			x = x-7
			paths.append(3)
		else:
			v1 = v1-6
			x = x-4
			i8 = i8-7
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