import numpy as np 

def function(x):

	n7 = x
	e7 = 4
	paths = []
	try:
		if x < 3:
			x = 4+e7
			paths.append(1)
		else:
			e7 = x/4
			x = x-x
			paths.append(2)
		if x >= 5:
			e7 = 9*6
			x = e7+n7
			e7 = x/3
			paths.append(3)
		else:
			x = 5*5
			e7 = e7/e7
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