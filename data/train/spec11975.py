import numpy as np 

def function(x):

	s2 = x
	g4 = 6
	paths = []
	try:
		if x < 8:
			x = 7/x
			x = x/5
			paths.append(1)
		else:
			s2 = s2+x
			s2 = 6*s2
			paths.append(2)
		if g4 > 3:
			g4 = g4-8
			s2 = 5/s2
			g4 = s2*g4
			paths.append(3)
		else:
			s2 = s2/4
			s2 = s2+x
			x = x/6
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))