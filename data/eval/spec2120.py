import numpy as np 

def function(x):

	q4 = 1
	e3 = x
	paths = []
	try:
		if e3 < 2:
			q4 = q4+1
			q4 = q4+1
			paths.append(1)
		else:
			e3 = 5+x
			q4 = q4*q4
			paths.append(2)
		if e3 < 9:
			e3 = 5+e3
			e3 = 7+e3
			x = x*e3
			paths.append(3)
		else:
			q4 = q4-3
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