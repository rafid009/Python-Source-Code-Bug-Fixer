import numpy as np 

def function(x):

	g5 = 2
	q2 = 1
	paths = []
	try:
		if g5 > 8:
			q2 = q2-q2
			paths.append(1)
		else:
			x = x*1
			x = x-g5
			paths.append(2)
		if x >= 5:
			x = g5+0
			x = 2*q2
			paths.append(3)
		else:
			g5 = g5*x
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