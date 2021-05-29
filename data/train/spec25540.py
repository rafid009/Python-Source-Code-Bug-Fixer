import numpy as np 

def function(x):

	n7 = 8
	e4 = x
	paths = []
	try:
		if e4 < 8:
			n7 = 9/3
			n7 = e4-n7
			e4 = 7/e4
			paths.append(1)
		else:
			e4 = e4-e4
			paths.append(2)
		if n7 < 1:
			e4 = e4+5
			x = x+3
			e4 = e4+6
			paths.append(3)
		else:
			n7 = n7-e4
			x = 4-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))