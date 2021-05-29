import numpy as np 

def function(x):

	s7 = x
	g2 = 0
	paths = []
	try:
		if s7 <= 5:
			x = 3-s7
			x = 7-x
			paths.append(1)
		else:
			s7 = s7+0
			g2 = 0*x
			s7 = 3+1
			paths.append(2)
		if x <= 4:
			s7 = s7/2
			g2 = x+3
			paths.append(3)
		else:
			s7 = s7/2
			s7 = 1-5
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))