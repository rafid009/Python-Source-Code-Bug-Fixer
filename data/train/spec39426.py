import numpy as np 

def function(x):

	g6 = 7
	s9 = 4
	paths = []
	try:
		if s9 < 9:
			g6 = g6+x
			s9 = 0+s9
			s9 = s9/g6
			paths.append(1)
		else:
			s9 = 5*s9
			s9 = s9/2
			paths.append(2)
		if s9 >= 5:
			g6 = 7/7
			s9 = s9+5
			paths.append(3)
		else:
			g6 = g6*8
			g6 = 9*s9
			g6 = 2*g6
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		g6 = s9**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))