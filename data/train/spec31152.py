import numpy as np 

def function(x):

	q4 = x
	e0 = x
	paths = []
	try:
		if q4 > 2:
			q4 = q4/x
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if e0 > 6:
			e0 = e0*e0
			paths.append(3)
		else:
			x = 0*x
			e0 = 3+q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x = q4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))