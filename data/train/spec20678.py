import numpy as np 

def function(x):

	q3 = 1
	e7 = x
	paths = []
	try:
		if x >= 6:
			q3 = 0/q3
			paths.append(1)
		else:
			e7 = e7-1
			paths.append(2)
		if x <= 2:
			e7 = 2*e7
			q3 = 7+3
			paths.append(3)
		else:
			q3 = q3*2
			q3 = x*q3
			e7 = e7+q3
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