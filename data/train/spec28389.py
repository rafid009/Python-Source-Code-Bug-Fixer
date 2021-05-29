import numpy as np 

def function(x):

	s1 = 3
	u7 = x
	paths = []
	try:
		if u7 >= 3:
			s1 = 7+s1
			s1 = u7-s1
			s1 = 7/1
			paths.append(1)
		else:
			x = 6/u7
			u7 = 2+u7
			s1 = 3*6
			paths.append(2)
		if s1 <= 3:
			s1 = 1+s1
			x = 1+x
			paths.append(3)
		else:
			x = 1+4
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		s1 = u7**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))