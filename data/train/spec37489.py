import numpy as np 

def function(x):

	x9 = x
	p0 = 7
	paths = []
	try:
		if x9 >= 3:
			x = x-0
			paths.append(1)
		else:
			x = x-8
			x9 = 4*x9
			paths.append(2)
		if x <= 4:
			x9 = x9-8
			paths.append(3)
		else:
			x9 = x9-9
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