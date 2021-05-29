import numpy as np 

def function(x):

	x5 = x
	s8 = 4
	paths = []
	try:
		if s8 > 0:
			x5 = 6/x5
			x = x/s8
			s8 = s8*9
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x5 < 3:
			x = 6+8
			paths.append(3)
		else:
			x5 = 6/x5
			s8 = s8-9
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))