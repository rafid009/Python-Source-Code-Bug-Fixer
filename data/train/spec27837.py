import numpy as np 

def function(x):

	y6 = x
	s5 = 6
	paths = []
	try:
		if y6 <= 2:
			s5 = 3-s5
			y6 = y6+9
			paths.append(1)
		else:
			y6 = 3/y6
			s5 = s5/s5
			s5 = 1-s5
			paths.append(2)
		if x >= 2:
			y6 = 2+s5
			s5 = s5+3
			s5 = s5/9
			paths.append(3)
		else:
			y6 = s5+y6
			y6 = 9-8
			y6 = 4*y6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))