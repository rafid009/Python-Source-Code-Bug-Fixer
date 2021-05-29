import numpy as np 

def function(x):

	s2 = 7
	g5 = x
	paths = []
	try:
		if g5 <= 2:
			g5 = s2+g5
			s2 = s2*s2
			paths.append(1)
		else:
			s2 = x+6
			paths.append(2)
		if g5 > 3:
			g5 = 5+6
			g5 = 9-9
			paths.append(3)
		else:
			x = g5-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))