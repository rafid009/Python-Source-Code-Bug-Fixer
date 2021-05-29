import numpy as np 

def function(x):

	a4 = 1
	s8 = x
	paths = []
	try:
		if s8 >= 5:
			x = a4*s8
			x = s8*7
			x = 3/x
			paths.append(1)
		else:
			a4 = a4+0
			x = x-7
			a4 = s8/a4
			paths.append(2)
		if s8 > 8:
			a4 = a4+5
			s8 = s8-4
			paths.append(3)
		else:
			a4 = x+0
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