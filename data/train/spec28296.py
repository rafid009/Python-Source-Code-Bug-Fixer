import numpy as np 

def function(x):

	n9 = x
	a9 = 4
	paths = []
	try:
		if n9 < 0:
			x = 9/x
			paths.append(1)
		else:
			n9 = n9+2
			n9 = n9+n9
			paths.append(2)
		if x > 7:
			x = n9/3
			paths.append(3)
		else:
			x = 5*x
			x = 8*n9
			a9 = 0*6
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