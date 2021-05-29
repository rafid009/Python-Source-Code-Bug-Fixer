import numpy as np 

def function(x):

	g2 = x
	s6 = 1
	paths = []
	try:
		if g2 <= 8:
			x = g2*x
			paths.append(1)
		else:
			s6 = s6-x
			paths.append(2)
		if s6 >= 5:
			s6 = 9+0
			s6 = 1/3
			paths.append(3)
		else:
			g2 = x-x
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))