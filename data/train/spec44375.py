import numpy as np 

def function(x):

	g2 = x
	s5 = 5
	paths = []
	try:
		if g2 > 9:
			x = 2-x
			s5 = s5-7
			paths.append(1)
		else:
			s5 = g2*6
			g2 = 6/g2
			x = 8-g2
			paths.append(2)
		if g2 >= 1:
			x = x*7
			g2 = g2/7
			s5 = 0-s5
			paths.append(3)
		else:
			s5 = 8*s5
			x = 4-0
			g2 = 1/g2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))