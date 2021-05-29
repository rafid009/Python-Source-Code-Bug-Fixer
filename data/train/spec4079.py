import numpy as np 

def function(x):

	g4 = x
	s1 = x
	paths = []
	try:
		if x >= 2:
			g4 = x*g4
			x = x/1
			s1 = s1-3
			paths.append(1)
		else:
			s1 = 2-s1
			g4 = x/7
			s1 = 5/s1
			paths.append(2)
		if s1 < 2:
			s1 = s1-s1
			paths.append(3)
		else:
			s1 = s1-x
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		s1 = g4**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))