import numpy as np 

def function(x):

	s8 = x
	g5 = x
	paths = []
	try:
		if x <= 3:
			s8 = 0/9
			paths.append(1)
		else:
			s8 = 2-g5
			x = 9*x
			paths.append(2)
		if g5 >= 2:
			s8 = s8-9
			g5 = g5-9
			paths.append(3)
		else:
			g5 = g5*g5
			g5 = 3-g5
			g5 = g5/x
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