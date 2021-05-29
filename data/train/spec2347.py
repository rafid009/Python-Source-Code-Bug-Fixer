import numpy as np 

def function(x):

	v5 = 8
	g5 = 2
	paths = []
	try:
		if v5 < 0:
			g5 = 5-g5
			x = 6*x
			g5 = g5/g5
			paths.append(1)
		else:
			g5 = v5*1
			paths.append(2)
		if x < 7:
			g5 = g5+6
			g5 = 3+4
			paths.append(3)
		else:
			x = 0-0
			g5 = g5-0
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