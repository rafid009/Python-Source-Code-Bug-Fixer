import numpy as np 

def function(x):

	s5 = 7
	g4 = 2
	paths = []
	try:
		if s5 > 1:
			x = x/1
			paths.append(1)
		else:
			g4 = g4*3
			s5 = s5*3
			s5 = g4/x
			paths.append(2)
		if x >= 3:
			x = 5-9
			s5 = s5+s5
			paths.append(3)
		else:
			x = x/8
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