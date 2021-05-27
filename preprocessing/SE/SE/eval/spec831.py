import numpy as np 

def function(x):

	i4 = 1
	s8 = x
	paths = []
	try:
		if i4 < 7:
			i4 = 6+6
			x = 9+x
			x = 7/x
			paths.append(1)
		else:
			s8 = 6+4
			s8 = s8*7
			x = i4-9
			paths.append(2)
		if s8 <= 8:
			i4 = 4+x
			paths.append(3)
		else:
			x = x+2
			s8 = s8*1
			s8 = s8-3
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