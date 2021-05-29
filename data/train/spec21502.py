import numpy as np 

def function(x):

	g6 = 7
	g5 = 3
	paths = []
	try:
		if x > 4:
			g5 = x+3
			g5 = g5*x
			paths.append(1)
		else:
			g5 = x*8
			paths.append(2)
		if g5 <= 6:
			g5 = 4*g5
			g6 = g5+g6
			paths.append(3)
		else:
			g6 = x+9
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