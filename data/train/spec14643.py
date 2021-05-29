import numpy as np 

def function(x):

	y0 = 4
	s6 = 9
	paths = []
	try:
		if s6 < 9:
			s6 = 2*s6
			paths.append(1)
		else:
			s6 = 2/s6
			x = x*1
			y0 = 4/y0
			paths.append(2)
		if y0 <= 6:
			s6 = s6-s6
			y0 = x/y0
			y0 = 0+y0
			paths.append(3)
		else:
			y0 = x*4
			s6 = 7+1
			y0 = y0/y0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		s6 = y0**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))