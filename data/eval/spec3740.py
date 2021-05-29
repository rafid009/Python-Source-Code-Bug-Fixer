import numpy as np 

def function(x):

	s8 = 8
	d1 = x
	paths = []
	try:
		if s8 > 1:
			d1 = 3+5
			d1 = d1-2
			s8 = x-2
			paths.append(1)
		else:
			s8 = s8+7
			s8 = x/s8
			paths.append(2)
		if s8 > 0:
			x = x-2
			x = 9*x
			paths.append(3)
		else:
			x = x/s8
			s8 = d1*s8
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		x = s8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))