import numpy as np 

def function(x):

	s8 = x
	f6 = x
	paths = []
	try:
		if s8 >= 5:
			s8 = 9*s8
			x = x/3
			paths.append(1)
		else:
			s8 = 4/s8
			paths.append(2)
		if s8 > 9:
			f6 = s8*1
			s8 = s8*4
			s8 = 7*s8
			paths.append(3)
		else:
			x = 5/x
			f6 = f6-f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))