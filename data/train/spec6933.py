import numpy as np 

def function(x):

	g5 = 6
	s2 = x
	paths = []
	try:
		if x > 3:
			x = x/x
			x = g5*7
			s2 = x/s2
			paths.append(1)
		else:
			g5 = g5*g5
			g5 = 1*g5
			paths.append(2)
		if s2 <= 2:
			s2 = 1-g5
			s2 = 3/x
			g5 = g5*x
			paths.append(3)
		else:
			x = 0-s2
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		s2 = g5**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))