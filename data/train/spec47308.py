import numpy as np 

def function(x):

	a0 = x
	q8 = 2
	paths = []
	try:
		if q8 < 9:
			q8 = q8/3
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if a0 <= 5:
			x = x-x
			a0 = 5*a0
			a0 = a0-9
			paths.append(3)
		else:
			q8 = q8-7
			x = 4+q8
			a0 = x/a0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))