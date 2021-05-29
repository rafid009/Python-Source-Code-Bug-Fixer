import numpy as np 

def function(x):

	i1 = x
	n0 = 1
	paths = []
	try:
		if x <= 2:
			i1 = 4+i1
			paths.append(1)
		else:
			x = 6/x
			x = x-8
			paths.append(2)
		if x < 4:
			n0 = 1-i1
			i1 = i1*4
			n0 = n0*6
			paths.append(3)
		else:
			x = 7-x
			i1 = i1*6
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