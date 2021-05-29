import numpy as np 

def function(x):

	s7 = x
	g0 = 1
	paths = []
	try:
		if x > 2:
			g0 = 7/g0
			g0 = 0+g0
			paths.append(1)
		else:
			x = x*8
			g0 = 3/x
			paths.append(2)
		if g0 >= 5:
			g0 = s7+g0
			paths.append(3)
		else:
			g0 = x/x
			g0 = g0-g0
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))