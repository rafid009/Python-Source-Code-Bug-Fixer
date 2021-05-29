import numpy as np 

def function(x):

	n7 = x
	n0 = x
	x = 2
	paths = []
	try:
		if n0 >= 8:
			n7 = 1-n7
			paths.append(1)
		else:
			x = 4-4
			paths.append(2)
		if x > 6:
			n0 = 3+n0
			paths.append(3)
		else:
			n0 = n0*9
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))