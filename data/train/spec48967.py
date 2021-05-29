import numpy as np 

def function(x):

	s5 = x
	g3 = x
	x = x
	paths = []
	try:
		if g3 <= 9:
			x = s5+5
			x = g3*s5
			paths.append(1)
		else:
			g3 = g3/5
			x = x+7
			paths.append(2)
		if g3 <= 0:
			x = 4/g3
			s5 = s5-x
			paths.append(3)
		else:
			s5 = 7/s5
			s5 = 6/s5
			x = 2-s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))