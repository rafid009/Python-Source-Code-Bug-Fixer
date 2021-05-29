import numpy as np 

def function(x):

	s4 = x
	x8 = 3
	x = 3
	paths = []
	try:
		if x8 > 9:
			x8 = s4-x8
			x8 = x8/x8
			s4 = s4+x
			paths.append(1)
		else:
			s4 = s4/x
			paths.append(2)
		if x8 >= 1:
			s4 = s4-6
			s4 = s4-x8
			paths.append(3)
		else:
			x8 = x8*7
			x = 2/x
			s4 = x/7
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))