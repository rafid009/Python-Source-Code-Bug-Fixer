import numpy as np 

def function(x):

	s0 = x
	g8 = 6
	paths = []
	try:
		if x <= 0:
			g8 = g8+g8
			g8 = g8*4
			x = x-0
			paths.append(1)
		else:
			x = s0-2
			s0 = s0+5
			g8 = g8*0
			paths.append(2)
		if x < 1:
			g8 = g8+4
			paths.append(3)
		else:
			x = s0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))