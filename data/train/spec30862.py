import numpy as np 

def function(x):

	n6 = 4
	a0 = 3
	paths = []
	try:
		if a0 <= 1:
			x = 4+x
			x = 3/x
			a0 = a0-5
			paths.append(1)
		else:
			a0 = 5*a0
			a0 = n6-0
			n6 = n6/9
			paths.append(2)
		if n6 > 7:
			x = x*9
			paths.append(3)
		else:
			n6 = n6*9
			a0 = a0-x
			n6 = 3*n6
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