import numpy as np 

def function(x):

	g9 = x
	s1 = x
	paths = []
	try:
		if s1 < 0:
			x = 4*x
			g9 = 1-g9
			s1 = s1-x
			paths.append(1)
		else:
			s1 = s1+2
			x = 4*x
			g9 = g9*g9
			paths.append(2)
		if s1 <= 8:
			x = x+x
			s1 = x*9
			paths.append(3)
		else:
			g9 = g9*g9
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))