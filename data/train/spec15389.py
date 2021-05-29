import numpy as np 

def function(x):

	n4 = 7
	x0 = 5
	paths = []
	try:
		if x0 > 1:
			x0 = 1/n4
			paths.append(1)
		else:
			x = n4*2
			paths.append(2)
		if x0 < 1:
			x = x+x
			x = n4+n4
			x = 9-x
			paths.append(3)
		else:
			x0 = x0*6
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