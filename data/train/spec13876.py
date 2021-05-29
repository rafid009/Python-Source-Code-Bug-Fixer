import numpy as np 

def function(x):

	g9 = 8
	q2 = 5
	paths = []
	try:
		if q2 > 0:
			g9 = g9/2
			q2 = q2*q2
			x = 7/x
			paths.append(1)
		else:
			q2 = 8+q2
			x = g9+7
			x = g9-4
			paths.append(2)
		if x >= 6:
			q2 = 1*q2
			g9 = g9/x
			g9 = g9-4
			paths.append(3)
		else:
			g9 = 1+g9
			g9 = g9-9
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