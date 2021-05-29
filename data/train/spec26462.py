import numpy as np 

def function(x):

	s5 = x
	g8 = 9
	paths = []
	try:
		if s5 > 5:
			g8 = x*5
			s5 = 9*x
			paths.append(1)
		else:
			g8 = 7-g8
			g8 = g8*3
			s5 = s5*8
			paths.append(2)
		if x < 8:
			g8 = g8/x
			paths.append(3)
		else:
			g8 = 2/s5
			g8 = x*x
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		g8 = s5**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))