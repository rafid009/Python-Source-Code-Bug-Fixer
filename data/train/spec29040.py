import numpy as np 

def function(x):

	b7 = 6
	s8 = x
	x = 2
	paths = []
	try:
		if b7 <= 4:
			s8 = s8/x
			s8 = s8+b7
			paths.append(1)
		else:
			s8 = 7-s8
			paths.append(2)
		if x < 8:
			b7 = 4+s8
			b7 = 0+8
			s8 = x-b7
			paths.append(3)
		else:
			s8 = 8/s8
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