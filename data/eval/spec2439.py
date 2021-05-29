import numpy as np 

def function(x):

	x8 = 2
	a6 = x
	paths = []
	try:
		if a6 > 0:
			a6 = 0/a6
			x8 = 4-a6
			paths.append(1)
		else:
			x = x8-2
			paths.append(2)
		if x >= 2:
			a6 = 5*x
			paths.append(3)
		else:
			x8 = x8*9
			x8 = 8*8
			x = 1+a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))