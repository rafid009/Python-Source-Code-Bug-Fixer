import numpy as np 

def function(x):

	q8 = x
	u0 = x
	x = x
	paths = []
	try:
		if q8 < 2:
			x = 0*x
			u0 = u0/u0
			u0 = u0-q8
			paths.append(1)
		else:
			x = 9*7
			u0 = 3*u0
			paths.append(2)
		if q8 >= 3:
			q8 = 2+6
			q8 = q8/2
			x = x+7
			paths.append(3)
		else:
			x = q8+x
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		q8 = u0**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))