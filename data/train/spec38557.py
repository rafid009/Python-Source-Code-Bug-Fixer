import numpy as np 

def function(x):

	x9 = 6
	a3 = x
	paths = []
	try:
		if x9 >= 2:
			a3 = 5*a3
			paths.append(1)
		else:
			x9 = x9*8
			paths.append(2)
		if x < 6:
			a3 = a3+2
			x9 = x9*x9
			x9 = x+x9
			paths.append(3)
		else:
			x = x+x
			x9 = a3/a3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))