import numpy as np 

def function(x):

	u2 = 2
	g5 = 8
	paths = []
	try:
		if x <= 9:
			x = x+5
			g5 = g5*x
			u2 = u2/6
			paths.append(1)
		else:
			g5 = g5/1
			x = x/u2
			paths.append(2)
		if x < 5:
			u2 = u2/2
			paths.append(3)
		else:
			g5 = 1+0
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