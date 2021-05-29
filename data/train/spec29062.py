import numpy as np 

def function(x):

	s0 = x
	g7 = 8
	paths = []
	try:
		if s0 >= 0:
			s0 = 5*6
			g7 = 9/g7
			x = s0/g7
			paths.append(1)
		else:
			s0 = g7+0
			paths.append(2)
		if g7 <= 1:
			s0 = s0-8
			s0 = 7/s0
			g7 = g7-0
			paths.append(3)
		else:
			g7 = x+7
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x = g7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))