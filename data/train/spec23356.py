import numpy as np 

def function(x):

	a7 = 9
	a3 = 1
	paths = []
	try:
		if a3 > 2:
			x = 9-0
			x = x+a3
			x = x*a3
			paths.append(1)
		else:
			x = x/a3
			paths.append(2)
		if a7 < 3:
			a3 = 9-a3
			a3 = a3+a7
			paths.append(3)
		else:
			a3 = x+a3
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