import numpy as np 

def function(x):

	s8 = x
	y8 = 3
	paths = []
	try:
		if s8 <= 8:
			y8 = 6+1
			y8 = 5+y8
			s8 = s8+y8
			paths.append(1)
		else:
			x = 8*x
			x = 6/2
			x = x/1
			paths.append(2)
		if s8 < 4:
			y8 = 8/y8
			s8 = y8/x
			s8 = s8+0
			paths.append(3)
		else:
			x = y8*1
			s8 = s8-7
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