import numpy as np 

def function(x):

	u6 = x
	s8 = 3
	paths = []
	try:
		if s8 >= 4:
			s8 = x*9
			x = x/x
			paths.append(1)
		else:
			s8 = 2*s8
			s8 = s8-7
			x = 9+6
			paths.append(2)
		if u6 >= 8:
			x = x-8
			s8 = 9-s8
			paths.append(3)
		else:
			u6 = u6-x
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		s8 = u6**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))