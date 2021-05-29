import numpy as np 

def function(x):

	s0 = 2
	y3 = 6
	paths = []
	try:
		if s0 >= 0:
			y3 = x*y3
			x = x*7
			x = x/y3
			paths.append(1)
		else:
			x = 0*9
			s0 = 7-0
			x = x-3
			paths.append(2)
		if x >= 3:
			y3 = y3/8
			s0 = s0+1
			x = x-9
			paths.append(3)
		else:
			s0 = 6*2
			y3 = y3+y3
			x = x/8
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))