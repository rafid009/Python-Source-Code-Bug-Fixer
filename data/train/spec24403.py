import numpy as np 

def function(x):

	g5 = x
	g1 = 5
	paths = []
	try:
		if x <= 5:
			g5 = g5+x
			g5 = 4*g5
			paths.append(1)
		else:
			g5 = g5/4
			g5 = x-8
			x = x*x
			paths.append(2)
		if x <= 9:
			g1 = 5-x
			g5 = x+5
			g5 = 1+g1
			paths.append(3)
		else:
			g5 = 6+g5
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