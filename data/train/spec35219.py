import numpy as np 

def function(x):

	s2 = 8
	g2 = 6
	paths = []
	try:
		if s2 <= 4:
			s2 = s2/5
			s2 = g2-2
			s2 = 7*5
			paths.append(1)
		else:
			g2 = 5*g2
			g2 = 8+7
			s2 = s2-9
			paths.append(2)
		if s2 > 8:
			s2 = 4+4
			g2 = g2*1
			paths.append(3)
		else:
			g2 = 3*g2
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		g2 = s2**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))