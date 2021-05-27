import numpy as np 

def function(x):

	s2 = x
	g3 = 9
	paths = []
	try:
		if x <= 7:
			g3 = 1-2
			paths.append(1)
		else:
			s2 = 4/7
			paths.append(2)
		if s2 < 7:
			x = 9/x
			paths.append(3)
		else:
			s2 = s2-x
			s2 = g3/s2
			s2 = 2*7
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))