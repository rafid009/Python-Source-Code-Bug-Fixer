import numpy as np 

def function(x):

	a8 = x
	n0 = 7
	paths = []
	try:
		if x <= 9:
			n0 = n0*6
			paths.append(1)
		else:
			n0 = n0-0
			a8 = 9*a8
			a8 = 5-a8
			paths.append(2)
		if n0 <= 8:
			n0 = n0*6
			paths.append(3)
		else:
			n0 = 3/a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))