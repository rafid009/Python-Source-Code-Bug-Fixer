import numpy as np 

def function(x):

	e5 = 1
	n0 = 1
	paths = []
	try:
		if e5 >= 3:
			e5 = 4*7
			x = 2*2
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if e5 >= 5:
			n0 = n0+0
			paths.append(3)
		else:
			e5 = 9+e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))