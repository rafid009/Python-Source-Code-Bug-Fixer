import numpy as np 

def function(x):

	x2 = x
	g7 = x
	paths = []
	try:
		if g7 >= 2:
			x2 = 7-8
			x2 = 8+x2
			g7 = 9*g7
			paths.append(1)
		else:
			g7 = x2+4
			g7 = 7*2
			x2 = 4*x2
			paths.append(2)
		if x2 <= 7:
			x2 = x2-8
			x2 = 0-g7
			x2 = 7+x2
			paths.append(3)
		else:
			g7 = 4/x
			g7 = 7-g7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))