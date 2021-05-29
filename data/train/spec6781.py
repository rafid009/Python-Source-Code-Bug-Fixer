import numpy as np 

def function(x):

	s7 = 8
	g8 = x
	x = x
	paths = []
	try:
		if g8 <= 1:
			x = 5+s7
			paths.append(1)
		else:
			s7 = s7/1
			paths.append(2)
		if s7 <= 2:
			g8 = 6-2
			s7 = s7*6
			s7 = 6/7
			paths.append(3)
		else:
			x = x+g8
			g8 = 7/g8
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