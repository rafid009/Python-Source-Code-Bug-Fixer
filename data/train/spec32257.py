import numpy as np 

def function(x):

	s0 = x
	y2 = 5
	paths = []
	try:
		if x <= 3:
			y2 = 8+4
			paths.append(1)
		else:
			y2 = 1/y2
			x = x+s0
			y2 = 5-y2
			paths.append(2)
		if s0 <= 0:
			s0 = 4*y2
			x = x*5
			paths.append(3)
		else:
			y2 = 6/y2
			y2 = s0/1
			s0 = s0+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))