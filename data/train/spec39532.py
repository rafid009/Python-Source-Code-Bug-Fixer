import numpy as np 

def function(x):

	g6 = x
	s4 = x
	paths = []
	try:
		if g6 > 2:
			x = 0-2
			x = x-5
			paths.append(1)
		else:
			s4 = 6-s4
			s4 = g6-9
			paths.append(2)
		if g6 <= 4:
			g6 = x+g6
			s4 = s4/7
			g6 = 6-x
			paths.append(3)
		else:
			s4 = s4*g6
			x = 3/4
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