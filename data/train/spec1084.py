import numpy as np 

def function(x):

	q1 = x
	g5 = x
	x = 0
	paths = []
	try:
		if x >= 4:
			x = 4*x
			paths.append(1)
		else:
			g5 = 1/g5
			x = x-2
			g5 = 6*x
			paths.append(2)
		if x > 1:
			q1 = q1*q1
			q1 = 0+q1
			x = g5-g5
			paths.append(3)
		else:
			x = x/4
			q1 = q1+9
			g5 = g5+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))