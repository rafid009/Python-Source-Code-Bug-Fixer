import numpy as np 

def function(x):

	g6 = x
	s1 = x
	paths = []
	try:
		if g6 <= 4:
			s1 = s1*8
			s1 = x*9
			paths.append(1)
		else:
			g6 = g6+5
			s1 = x+s1
			paths.append(2)
		if g6 > 2:
			g6 = x+g6
			g6 = x/5
			paths.append(3)
		else:
			s1 = 8-1
			g6 = g6*g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))