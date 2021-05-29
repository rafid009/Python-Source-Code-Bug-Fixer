import numpy as np 

def function(x):

	t4 = x
	s8 = x
	paths = []
	try:
		if s8 >= 5:
			x = x*4
			s8 = 3*5
			paths.append(1)
		else:
			x = s8+6
			s8 = s8-8
			x = 2/x
			paths.append(2)
		if x < 0:
			s8 = t4*s8
			x = x/t4
			paths.append(3)
		else:
			s8 = s8/7
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