import numpy as np 

def function(x):

	i0 = x
	s2 = x
	paths = []
	try:
		if s2 < 3:
			x = 5-x
			i0 = i0+5
			s2 = s2/i0
			paths.append(1)
		else:
			i0 = i0-5
			s2 = x-1
			i0 = i0-2
			paths.append(2)
		if s2 < 1:
			s2 = s2-i0
			x = s2/8
			paths.append(3)
		else:
			s2 = 4+i0
			s2 = 5+s2
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