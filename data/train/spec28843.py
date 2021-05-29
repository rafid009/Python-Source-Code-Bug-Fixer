import numpy as np 

def function(x):

	a9 = x
	n4 = 8
	paths = []
	try:
		if n4 < 7:
			x = x-4
			paths.append(1)
		else:
			x = 3*x
			n4 = n4-2
			a9 = 0*a9
			paths.append(2)
		if n4 < 9:
			a9 = x*x
			paths.append(3)
		else:
			x = 6+x
			a9 = a9-x
			n4 = n4+n4
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