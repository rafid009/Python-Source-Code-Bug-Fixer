import numpy as np 

def function(x):

	c0 = x
	s5 = x
	paths = []
	try:
		if s5 < 7:
			c0 = c0+3
			paths.append(1)
		else:
			s5 = s5+7
			s5 = s5*3
			paths.append(2)
		if s5 >= 7:
			c0 = c0+8
			c0 = s5-s5
			c0 = c0+s5
			paths.append(3)
		else:
			s5 = s5/4
			x = x-1
			s5 = c0+7
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