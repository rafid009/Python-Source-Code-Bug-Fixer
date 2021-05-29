import numpy as np 

def function(x):

	s0 = 0
	g3 = 8
	paths = []
	try:
		if g3 < 3:
			g3 = g3*5
			s0 = s0-8
			g3 = g3+6
			paths.append(1)
		else:
			s0 = 0+s0
			paths.append(2)
		if g3 <= 5:
			s0 = s0*1
			x = 1/g3
			paths.append(3)
		else:
			g3 = 2-s0
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