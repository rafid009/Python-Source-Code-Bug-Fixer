import numpy as np 

def function(x):

	e7 = x
	q0 = x
	x = x
	paths = []
	try:
		if q0 > 5:
			q0 = e7-q0
			paths.append(1)
		else:
			q0 = q0/4
			q0 = 3/8
			x = x+9
			paths.append(2)
		if e7 >= 1:
			e7 = e7-4
			x = x/3
			paths.append(3)
		else:
			x = 4-x
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