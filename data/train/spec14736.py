import numpy as np 

def function(x):

	g8 = x
	s7 = 9
	paths = []
	try:
		if g8 <= 3:
			x = g8+0
			paths.append(1)
		else:
			g8 = 1-1
			s7 = s7/7
			paths.append(2)
		if x < 9:
			s7 = 1/1
			g8 = g8*s7
			paths.append(3)
		else:
			s7 = g8/9
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		s7 = g8**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))