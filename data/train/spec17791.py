import numpy as np 

def function(x):

	n1 = x
	a3 = x
	x = x
	paths = []
	try:
		if x < 6:
			a3 = x/4
			n1 = 2*3
			paths.append(1)
		else:
			a3 = 9-x
			paths.append(2)
		if x < 7:
			n1 = 1/x
			a3 = a3+n1
			paths.append(3)
		else:
			x = x+6
			x = n1*5
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