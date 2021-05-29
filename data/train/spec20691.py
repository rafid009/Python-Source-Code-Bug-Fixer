import numpy as np 

def function(x):

	q2 = x
	a5 = x
	paths = []
	try:
		if a5 < 0:
			x = 1-x
			q2 = 9-q2
			paths.append(1)
		else:
			a5 = 8/7
			q2 = q2/7
			paths.append(2)
		if a5 <= 9:
			x = 2/x
			x = 4-x
			paths.append(3)
		else:
			q2 = q2+7
			x = 0*a5
			a5 = a5*a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))