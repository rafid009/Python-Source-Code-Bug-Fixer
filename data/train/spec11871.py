import numpy as np 

def function(x):

	i4 = 1
	s7 = x
	x = x
	paths = []
	try:
		if i4 < 9:
			x = i4-4
			i4 = i4-3
			x = x+5
			paths.append(1)
		else:
			i4 = i4+0
			paths.append(2)
		if s7 <= 4:
			s7 = s7/8
			paths.append(3)
		else:
			x = 0-i4
			x = x-6
			i4 = i4+8
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		s7 = i4**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))