import numpy as np 

def function(x):

	e7 = x
	n7 = 7
	paths = []
	try:
		if x <= 9:
			e7 = e7-e7
			paths.append(1)
		else:
			n7 = n7*n7
			e7 = e7*4
			n7 = 8/n7
			paths.append(2)
		if n7 >= 9:
			x = e7-5
			x = x-7
			paths.append(3)
		else:
			n7 = n7-4
			n7 = n7-7
			n7 = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))