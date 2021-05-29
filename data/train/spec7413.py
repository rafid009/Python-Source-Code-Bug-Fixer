import numpy as np 

def function(x):

	s5 = 6
	g1 = x
	paths = []
	try:
		if x < 4:
			g1 = 0+6
			paths.append(1)
		else:
			x = x/x
			x = x+x
			x = 1/5
			paths.append(2)
		if g1 < 7:
			x = x+3
			paths.append(3)
		else:
			s5 = s5*6
			g1 = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))