import numpy as np 

def function(x):

	j0 = 3
	n6 = 1
	paths = []
	try:
		if x > 6:
			n6 = n6+6
			paths.append(1)
		else:
			j0 = j0-4
			j0 = j0/n6
			paths.append(2)
		if x < 7:
			n6 = 0/n6
			x = 8/x
			paths.append(3)
		else:
			x = x-x
			j0 = 9+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))