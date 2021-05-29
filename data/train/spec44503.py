import numpy as np 

def function(x):

	n6 = x
	z1 = x
	paths = []
	try:
		if z1 <= 3:
			n6 = x*3
			paths.append(1)
		else:
			n6 = x+4
			paths.append(2)
		if x <= 6:
			n6 = n6/9
			n6 = 2+8
			x = n6*x
			paths.append(3)
		else:
			n6 = 2+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))