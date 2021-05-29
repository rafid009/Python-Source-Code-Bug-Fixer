import numpy as np 

def function(x):

	e0 = x
	q6 = 3
	x = 0
	paths = []
	try:
		if q6 > 2:
			x = q6-e0
			q6 = 2-9
			e0 = x-e0
			paths.append(1)
		else:
			x = 7/4
			paths.append(2)
		if q6 < 6:
			x = x*4
			e0 = e0+8
			x = x/1
			paths.append(3)
		else:
			q6 = e0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))