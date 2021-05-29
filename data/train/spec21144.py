import numpy as np 

def function(x):

	s8 = 1
	r7 = x
	paths = []
	try:
		if x >= 6:
			r7 = 7*x
			x = r7/s8
			r7 = 9+r7
			paths.append(1)
		else:
			s8 = x/9
			s8 = s8*r7
			r7 = 5-s8
			paths.append(2)
		if s8 >= 1:
			r7 = r7*5
			s8 = s8*6
			paths.append(3)
		else:
			s8 = 4-s8
			x = 3*x
			x = s8+4
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