import numpy as np 

def function(x):

	e0 = 5
	q0 = 4
	paths = []
	try:
		if q0 <= 5:
			q0 = 0-q0
			q0 = 4+q0
			e0 = q0*e0
			paths.append(1)
		else:
			e0 = 0-e0
			paths.append(2)
		if x < 8:
			x = 9/x
			e0 = 8+2
			paths.append(3)
		else:
			q0 = 2+4
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