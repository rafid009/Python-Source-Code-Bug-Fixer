import numpy as np 

def function(x):

	q6 = x
	e3 = x
	paths = []
	try:
		if q6 <= 0:
			q6 = e3/5
			x = x-5
			e3 = 0-x
			paths.append(1)
		else:
			q6 = 4*1
			paths.append(2)
		if q6 > 3:
			e3 = 2/6
			paths.append(3)
		else:
			q6 = q6-x
			e3 = 7+e3
			x = x-e3
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