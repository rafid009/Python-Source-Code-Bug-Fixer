import numpy as np 

def function(x):

	g6 = 9
	s9 = x
	paths = []
	try:
		if s9 >= 1:
			s9 = s9-s9
			s9 = s9*g6
			x = x/3
			paths.append(1)
		else:
			s9 = 7*s9
			x = x/1
			paths.append(2)
		if g6 > 0:
			x = x-2
			paths.append(3)
		else:
			x = x*3
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