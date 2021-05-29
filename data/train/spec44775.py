import numpy as np 

def function(x):

	s2 = 0
	y8 = 3
	paths = []
	try:
		if y8 < 4:
			s2 = s2-s2
			s2 = s2+9
			s2 = s2/8
			paths.append(1)
		else:
			s2 = 2+s2
			s2 = x-s2
			y8 = 0+y8
			paths.append(2)
		if s2 <= 9:
			s2 = 1*y8
			paths.append(3)
		else:
			y8 = y8-2
			s2 = 5+3
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