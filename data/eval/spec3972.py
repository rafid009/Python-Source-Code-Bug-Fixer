import numpy as np 

def function(x):

	s1 = 5
	g7 = x
	paths = []
	try:
		if s1 < 7:
			s1 = x*7
			s1 = 0-g7
			paths.append(1)
		else:
			x = x+0
			s1 = s1+0
			g7 = g7-9
			paths.append(2)
		if g7 <= 3:
			g7 = x*g7
			paths.append(3)
		else:
			s1 = s1-1
			g7 = s1-g7
			s1 = x/g7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))