import numpy as np 

def function(x):

	x0 = x
	a0 = 2
	paths = []
	try:
		if x0 >= 3:
			x0 = 0*8
			paths.append(1)
		else:
			a0 = a0*x0
			a0 = a0+4
			paths.append(2)
		if x <= 9:
			a0 = a0-0
			paths.append(3)
		else:
			x0 = 8*x0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))