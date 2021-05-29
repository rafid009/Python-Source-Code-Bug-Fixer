import numpy as np 

def function(x):

	t2 = 3
	s8 = 6
	paths = []
	try:
		if s8 < 2:
			x = t2-5
			s8 = s8/3
			s8 = s8/7
			paths.append(1)
		else:
			s8 = t2-s8
			s8 = s8+s8
			paths.append(2)
		if x < 1:
			x = 5-x
			paths.append(3)
		else:
			t2 = s8+2
			s8 = 5-9
			s8 = 5+t2
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		s8 = s8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))