import numpy as np 

def function(x):

	g4 = 4
	s9 = x
	paths = []
	try:
		if x > 5:
			g4 = 2-7
			paths.append(1)
		else:
			g4 = g4/2
			g4 = g4+5
			paths.append(2)
		if s9 < 8:
			s9 = 9-s9
			x = 5*x
			g4 = 4+g4
			paths.append(3)
		else:
			g4 = g4*x
			s9 = s9*8
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))