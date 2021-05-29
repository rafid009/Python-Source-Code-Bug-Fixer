import numpy as np 

def function(x):

	e7 = 7
	q0 = 7
	paths = []
	try:
		if e7 < 2:
			x = q0+x
			paths.append(1)
		else:
			q0 = q0-7
			e7 = e7-0
			q0 = 9*q0
			paths.append(2)
		if e7 > 0:
			x = x+x
			q0 = q0+1
			paths.append(3)
		else:
			e7 = q0+e7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))