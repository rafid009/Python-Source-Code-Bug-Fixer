import numpy as np 

def function(x):

	q3 = 9
	g3 = x
	paths = []
	try:
		if g3 < 7:
			g3 = x*g3
			q3 = q3-q3
			g3 = 7*7
			paths.append(1)
		else:
			g3 = g3+g3
			paths.append(2)
		if g3 < 0:
			q3 = 6-q3
			paths.append(3)
		else:
			x = x/g3
			g3 = 9/g3
			g3 = g3-g3
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