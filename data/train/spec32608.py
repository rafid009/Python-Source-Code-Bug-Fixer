import numpy as np 

def function(x):

	g5 = x
	s2 = 0
	paths = []
	try:
		if g5 > 1:
			g5 = 9+g5
			s2 = s2-2
			paths.append(1)
		else:
			s2 = 3*s2
			paths.append(2)
		if s2 <= 0:
			x = x-2
			s2 = s2*2
			g5 = g5/3
			paths.append(3)
		else:
			x = 6*x
			s2 = 3+9
			s2 = 5-g5
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		g5 = s2**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))