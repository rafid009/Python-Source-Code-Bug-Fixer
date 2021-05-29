import numpy as np 

def function(x):

	a0 = 1
	x9 = x
	paths = []
	try:
		if a0 > 8:
			x = x+3
			x = a0+3
			paths.append(1)
		else:
			a0 = a0+a0
			a0 = 4-x
			a0 = x9-a0
			paths.append(2)
		if x >= 0:
			x = 3*x
			a0 = a0+4
			paths.append(3)
		else:
			x9 = 6+x9
			a0 = a0/6
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