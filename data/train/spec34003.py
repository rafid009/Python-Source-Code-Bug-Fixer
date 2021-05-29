import numpy as np 

def function(x):

	q0 = x
	g8 = x
	paths = []
	try:
		if g8 < 7:
			q0 = q0-3
			q0 = x+1
			paths.append(1)
		else:
			q0 = x/g8
			q0 = q0/g8
			x = x-6
			paths.append(2)
		if g8 <= 1:
			g8 = g8/8
			x = x+7
			paths.append(3)
		else:
			q0 = q0*x
			q0 = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))