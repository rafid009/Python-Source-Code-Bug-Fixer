import numpy as np 

def function(x):

	s8 = x
	s7 = x
	paths = []
	try:
		if s7 >= 4:
			s8 = 6+s8
			x = 7-x
			paths.append(1)
		else:
			s7 = s7*3
			s7 = 1-9
			s8 = s8/x
			paths.append(2)
		if x > 2:
			x = x*4
			s8 = 4*s8
			paths.append(3)
		else:
			s7 = s7*4
			x = x+0
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