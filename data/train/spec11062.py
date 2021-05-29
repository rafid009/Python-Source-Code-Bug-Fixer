import numpy as np 

def function(x):

	q2 = 6
	a9 = 8
	paths = []
	try:
		if q2 <= 0:
			q2 = q2-8
			q2 = q2*q2
			a9 = a9-2
			paths.append(1)
		else:
			a9 = 5-2
			paths.append(2)
		if a9 > 7:
			x = x*8
			q2 = q2-q2
			paths.append(3)
		else:
			a9 = a9*a9
			q2 = q2-q2
			x = a9-x
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