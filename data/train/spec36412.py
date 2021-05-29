import numpy as np 

def function(x):

	g6 = 2
	s9 = 6
	x = 4
	paths = []
	try:
		if x <= 6:
			s9 = s9+1
			x = x+1
			s9 = x*2
			paths.append(1)
		else:
			x = x+4
			g6 = 8-g6
			paths.append(2)
		if g6 >= 5:
			x = 9-g6
			paths.append(3)
		else:
			s9 = s9*3
			g6 = g6-8
			x = x/6
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))