import numpy as np 

def function(x):

	q3 = x
	e2 = 5
	x = x
	paths = []
	try:
		if x > 8:
			x = x/6
			q3 = 0/8
			paths.append(1)
		else:
			x = 7-x
			x = x-3
			paths.append(2)
		if q3 >= 8:
			x = x-x
			x = x-7
			q3 = q3/q3
			paths.append(3)
		else:
			e2 = 7+e2
			e2 = 0*e2
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))