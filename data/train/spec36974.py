import numpy as np 

def function(x):

	q9 = x
	a4 = 9
	paths = []
	try:
		if x < 5:
			x = 3*x
			q9 = 8/2
			paths.append(1)
		else:
			x = a4*q9
			a4 = a4+5
			paths.append(2)
		if q9 < 5:
			a4 = 1/x
			q9 = q9-8
			x = q9-x
			paths.append(3)
		else:
			a4 = 7*a4
			x = x/7
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