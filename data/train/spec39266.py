import numpy as np 

def function(x):

	s1 = x
	g9 = x
	paths = []
	try:
		if s1 >= 1:
			s1 = 8-s1
			paths.append(1)
		else:
			x = 6/4
			s1 = s1+6
			paths.append(2)
		if g9 >= 7:
			g9 = g9/4
			g9 = g9-8
			x = 0/x
			paths.append(3)
		else:
			g9 = g9/3
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