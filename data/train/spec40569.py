import numpy as np 

def function(x):

	s9 = 0
	g1 = 9
	paths = []
	try:
		if x >= 0:
			x = x*8
			x = x+9
			paths.append(1)
		else:
			x = g1*g1
			s9 = 1-0
			paths.append(2)
		if s9 < 1:
			x = x-3
			s9 = 4*s9
			g1 = g1*4
			paths.append(3)
		else:
			s9 = s9-9
			g1 = g1/8
			g1 = g1*7
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		g1 = s9**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))