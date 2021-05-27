import numpy as np 

def function(x):

	n3 = 3
	e4 = 9
	x = x
	paths = []
	try:
		if x >= 2:
			x = 7*e4
			paths.append(1)
		else:
			x = 9*x
			x = n3-5
			paths.append(2)
		if n3 > 4:
			n3 = 7*n3
			e4 = e4/n3
			x = x-8
			paths.append(3)
		else:
			e4 = x/4
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