import numpy as np 

def function(x):

	y2 = 9
	s8 = 6
	paths = []
	try:
		if s8 < 3:
			y2 = 7*y2
			s8 = 1-2
			y2 = s8+y2
			paths.append(1)
		else:
			y2 = s8+y2
			y2 = y2/x
			x = x/y2
			paths.append(2)
		if s8 > 3:
			s8 = s8+8
			y2 = y2+3
			paths.append(3)
		else:
			y2 = y2+5
			y2 = y2-3
			y2 = 7+2
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))