import numpy as np 

def function(x):

	g1 = x
	s8 = x
	paths = []
	try:
		if s8 > 6:
			s8 = 0+s8
			g1 = s8/g1
			paths.append(1)
		else:
			g1 = g1/4
			s8 = 2*x
			s8 = x+2
			paths.append(2)
		if g1 < 2:
			g1 = 1-3
			s8 = 5*6
			g1 = g1+g1
			paths.append(3)
		else:
			g1 = g1+x
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		s8 = g1**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))