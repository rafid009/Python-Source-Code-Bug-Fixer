import numpy as np 

def function(x):

	e3 = 6
	n3 = x
	x = x
	paths = []
	try:
		if n3 > 7:
			n3 = e3*n3
			paths.append(1)
		else:
			n3 = 1*n3
			x = n3-7
			n3 = 5/1
			paths.append(2)
		if n3 > 6:
			x = x-8
			paths.append(3)
		else:
			e3 = 9/n3
			x = x-1
			n3 = 3+n3
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