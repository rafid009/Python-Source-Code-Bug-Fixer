import numpy as np 

def function(x):

	s5 = x
	x = x
	paths = []
	try:
		if s5 < 0:
			x = s5+x
			s5 = 4/s5
			paths.append(1)
		else:
			s5 = s5+4
			s5 = 8+s5
			paths.append(2)
		if s5 >= 0:
			s5 = s5+s5
			s5 = 6-s5
			x = 5+x
			paths.append(3)
		else:
			s5 = s5*5
			s5 = s5*9
			x = x/8
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