import numpy as np 

def function(x):

	f8 = x
	s8 = 7
	paths = []
	try:
		if s8 > 4:
			s8 = 7-4
			paths.append(1)
		else:
			x = x-f8
			x = 2/2
			x = 1-x
			paths.append(2)
		if s8 < 3:
			f8 = x+f8
			x = 4-0
			paths.append(3)
		else:
			s8 = 2-f8
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