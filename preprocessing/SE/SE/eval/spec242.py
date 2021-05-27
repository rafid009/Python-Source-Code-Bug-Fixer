import numpy as np 

def function(x):

	s6 = 6
	g2 = 8
	paths = []
	try:
		if g2 < 2:
			x = x+x
			x = x+2
			g2 = 0/g2
			paths.append(1)
		else:
			x = x/3
			g2 = 3+g2
			paths.append(2)
		if g2 <= 0:
			s6 = s6+5
			s6 = g2/5
			paths.append(3)
		else:
			x = 0+x
			s6 = 3-s6
			s6 = s6+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))