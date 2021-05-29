import numpy as np 

def function(x):

	s5 = 5
	y6 = x
	paths = []
	try:
		if y6 < 9:
			s5 = 9-6
			paths.append(1)
		else:
			s5 = s5/s5
			paths.append(2)
		if s5 > 4:
			x = 5-4
			paths.append(3)
		else:
			y6 = s5+y6
			s5 = s5*y6
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))