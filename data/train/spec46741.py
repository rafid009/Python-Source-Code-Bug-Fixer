import numpy as np 

def function(x):

	n1 = x
	a7 = x
	paths = []
	try:
		if x >= 4:
			x = x/x
			paths.append(1)
		else:
			a7 = a7-2
			a7 = a7-6
			paths.append(2)
		if x <= 2:
			x = 2/x
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))