import numpy as np 

def function(x):

	n3 = x
	a4 = x
	paths = []
	try:
		if n3 < 0:
			a4 = a4-6
			n3 = 2/n3
			n3 = n3-7
			paths.append(1)
		else:
			a4 = 5+a4
			paths.append(2)
		if n3 > 1:
			n3 = a4/n3
			a4 = a4+8
			a4 = 6-x
			paths.append(3)
		else:
			x = 0*x
			x = x-n3
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