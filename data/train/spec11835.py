import numpy as np 

def function(x):

	y0 = x
	s6 = 4
	paths = []
	try:
		if s6 <= 7:
			y0 = y0/s6
			x = x/5
			paths.append(1)
		else:
			x = x+6
			y0 = x*y0
			y0 = 3-7
			paths.append(2)
		if y0 > 3:
			x = 2/y0
			s6 = s6-4
			s6 = 2-s6
			paths.append(3)
		else:
			x = y0+y0
			s6 = 2+x
			x = x*s6
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))