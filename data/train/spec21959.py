import numpy as np 

def function(x):

	s4 = x
	g5 = x
	paths = []
	try:
		if g5 > 3:
			g5 = g5+8
			g5 = s4/g5
			s4 = 9*s4
			paths.append(1)
		else:
			g5 = s4/7
			paths.append(2)
		if g5 > 6:
			g5 = g5+x
			x = g5+x
			g5 = 7/g5
			paths.append(3)
		else:
			x = 5+x
			s4 = x+s4
			x = x/6
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))