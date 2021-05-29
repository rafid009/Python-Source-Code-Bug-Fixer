import numpy as np 

def function(x):

	s4 = x
	g8 = x
	paths = []
	try:
		if x >= 1:
			s4 = 7/3
			g8 = s4+2
			x = 5+x
			paths.append(1)
		else:
			x = s4/4
			s4 = 0+x
			paths.append(2)
		if x > 0:
			s4 = g8*5
			s4 = 3/s4
			s4 = g8-s4
			paths.append(3)
		else:
			s4 = 9*8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))