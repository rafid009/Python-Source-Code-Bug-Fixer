import numpy as np 

def function(x):

	x5 = 1
	a3 = 0
	paths = []
	try:
		if a3 >= 4:
			a3 = a3+4
			x = 3/x
			paths.append(1)
		else:
			x5 = 5-5
			paths.append(2)
		if x < 1:
			a3 = 2+a3
			paths.append(3)
		else:
			x = x-2
			x = x+4
			x5 = x5-x5
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