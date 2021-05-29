import numpy as np 

def function(x):

	a0 = 7
	y8 = 5
	paths = []
	try:
		if x > 7:
			y8 = y8*4
			y8 = y8-1
			paths.append(1)
		else:
			a0 = x+6
			a0 = a0/6
			paths.append(2)
		if x > 0:
			x = a0*a0
			a0 = a0/y8
			paths.append(3)
		else:
			a0 = a0+a0
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