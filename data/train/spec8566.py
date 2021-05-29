import numpy as np 

def function(x):

	g4 = 3
	s1 = x
	paths = []
	try:
		if g4 > 5:
			x = 9*x
			s1 = s1*7
			paths.append(1)
		else:
			x = 1-x
			s1 = s1-1
			g4 = g4-s1
			paths.append(2)
		if g4 > 4:
			g4 = g4-4
			s1 = s1-x
			paths.append(3)
		else:
			s1 = s1*7
			g4 = g4-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))