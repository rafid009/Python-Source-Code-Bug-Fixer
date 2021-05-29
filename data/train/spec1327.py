import numpy as np 

def function(x):

	g9 = 7
	s4 = x
	paths = []
	try:
		if s4 >= 3:
			g9 = 7+g9
			s4 = s4+7
			x = x*s4
			paths.append(1)
		else:
			x = x+3
			g9 = 3+7
			paths.append(2)
		if s4 > 7:
			g9 = g9+3
			g9 = g9-0
			x = 8-s4
			paths.append(3)
		else:
			s4 = s4/9
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))