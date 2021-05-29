import numpy as np 

def function(x):

	g2 = 7
	s6 = 3
	x = x
	paths = []
	try:
		if x > 2:
			g2 = g2+6
			s6 = s6-3
			paths.append(1)
		else:
			g2 = 8/g2
			paths.append(2)
		if x <= 6:
			s6 = x-s6
			s6 = s6+5
			paths.append(3)
		else:
			s6 = g2+s6
			x = 3+s6
			g2 = 0-s6
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		g2 = s6**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))