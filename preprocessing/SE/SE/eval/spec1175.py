import numpy as np 

def function(x):

	s8 = 0
	g1 = 0
	x = 9
	paths = []
	try:
		if s8 >= 5:
			s8 = g1*s8
			x = x/6
			x = x-x
			paths.append(1)
		else:
			g1 = 9-g1
			x = 3-x
			s8 = x-7
			paths.append(2)
		if s8 < 3:
			g1 = g1/g1
			s8 = 2-9
			x = 8/8
			paths.append(3)
		else:
			g1 = 9*8
			x = s8+x
			x = x*1
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