import numpy as np 

def function(x):

	g4 = 5
	s7 = 8
	paths = []
	try:
		if g4 < 1:
			s7 = s7+s7
			g4 = g4+7
			g4 = g4/5
			paths.append(1)
		else:
			x = 0-1
			paths.append(2)
		if s7 > 8:
			g4 = g4/8
			paths.append(3)
		else:
			s7 = 0/x
			g4 = g4+g4
			s7 = s7+g4
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