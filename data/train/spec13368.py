import numpy as np 

def function(x):

	x4 = x
	a1 = x
	paths = []
	try:
		if x < 0:
			x4 = 1/x4
			paths.append(1)
		else:
			a1 = a1*6
			a1 = 7/a1
			paths.append(2)
		if x4 < 6:
			x = 0*x
			x = x-x4
			paths.append(3)
		else:
			a1 = x+x
			x = x4*x4
			a1 = 5/x
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