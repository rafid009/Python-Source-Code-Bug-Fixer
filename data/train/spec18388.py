import numpy as np 

def function(x):

	q2 = 4
	g7 = 9
	paths = []
	try:
		if g7 > 0:
			q2 = q2/7
			paths.append(1)
		else:
			q2 = q2*q2
			x = x*7
			paths.append(2)
		if g7 > 9:
			g7 = g7+g7
			paths.append(3)
		else:
			g7 = 4*g7
			x = x*4
			g7 = g7-0
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