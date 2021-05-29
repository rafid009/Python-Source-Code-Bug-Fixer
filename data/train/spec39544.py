import numpy as np 

def function(x):

	g8 = x
	s9 = x
	paths = []
	try:
		if g8 < 9:
			g8 = x+s9
			paths.append(1)
		else:
			s9 = g8/s9
			s9 = 6-s9
			paths.append(2)
		if g8 < 0:
			x = x-s9
			paths.append(3)
		else:
			x = 7-2
			s9 = 2/s9
			x = x-2
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		g8 = s9**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))