import numpy as np 

def function(x):

	s2 = x
	g7 = 3
	paths = []
	try:
		if x >= 5:
			s2 = s2/9
			s2 = 4*8
			paths.append(1)
		else:
			s2 = x/x
			x = 2-x
			g7 = x/s2
			paths.append(2)
		if x > 6:
			g7 = x/2
			g7 = g7*g7
			x = x*7
			paths.append(3)
		else:
			g7 = g7*1
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))