import numpy as np 

def function(x):

	r3 = x
	x0 = x
	paths = []
	try:
		if x >= 1:
			x0 = 4+x0
			paths.append(1)
		else:
			x0 = x-x0
			x = x0-4
			paths.append(2)
		if x > 9:
			r3 = 9-r3
			x0 = x+7
			paths.append(3)
		else:
			x0 = r3+6
			x = x-8
			x = 4/r3
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))