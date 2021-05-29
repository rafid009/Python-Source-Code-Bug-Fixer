import numpy as np 

def function(x):

	s6 = 9
	y4 = x
	paths = []
	try:
		if s6 >= 8:
			s6 = 0*y4
			s6 = 4+0
			paths.append(1)
		else:
			s6 = s6-8
			x = 6+6
			paths.append(2)
		if y4 <= 4:
			y4 = 1*y4
			y4 = y4-1
			paths.append(3)
		else:
			x = x-2
			s6 = y4/s6
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))