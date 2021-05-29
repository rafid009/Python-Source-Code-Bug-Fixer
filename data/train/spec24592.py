import numpy as np 

def function(x):

	e5 = 7
	g5 = x
	x = 8
	paths = []
	try:
		if g5 > 3:
			g5 = 9-g5
			x = g5/5
			paths.append(1)
		else:
			e5 = e5/5
			x = 5*e5
			x = x*e5
			paths.append(2)
		if e5 < 5:
			x = 0+x
			e5 = 1-e5
			e5 = 7+e5
			paths.append(3)
		else:
			g5 = g5*7
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