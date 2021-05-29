import numpy as np 

def function(x):

	s8 = 0
	y4 = 8
	paths = []
	try:
		if y4 < 7:
			s8 = 9/s8
			paths.append(1)
		else:
			y4 = 6+1
			s8 = s8+9
			y4 = y4*x
			paths.append(2)
		if s8 < 3:
			x = s8*0
			x = 5-s8
			paths.append(3)
		else:
			s8 = s8*y4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		s8 = y4**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))