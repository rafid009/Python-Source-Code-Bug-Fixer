import numpy as np 

def function(x):

	g7 = 8
	s5 = x
	x = x
	paths = []
	try:
		if s5 < 6:
			g7 = 8*g7
			x = 7*x
			g7 = 9-g7
			paths.append(1)
		else:
			g7 = 4/9
			paths.append(2)
		if x >= 4:
			g7 = 7-g7
			x = x*s5
			x = 4+8
			paths.append(3)
		else:
			g7 = 3/g7
			s5 = 4*s5
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