import numpy as np 

def function(x):

	x1 = x
	s8 = x
	paths = []
	try:
		if s8 < 6:
			x1 = x1-8
			s8 = 7+3
			paths.append(1)
		else:
			s8 = x/x
			x1 = x1*4
			s8 = s8+s8
			paths.append(2)
		if x <= 4:
			s8 = s8+1
			s8 = s8*8
			paths.append(3)
		else:
			s8 = s8-9
			x = x/x
			s8 = s8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))