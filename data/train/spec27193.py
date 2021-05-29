import numpy as np 

def function(x):

	s8 = 6
	o9 = x
	paths = []
	try:
		if s8 > 6:
			o9 = o9*8
			paths.append(1)
		else:
			x = x+o9
			o9 = 5-3
			paths.append(2)
		if o9 < 7:
			s8 = s8-4
			x = x+o9
			paths.append(3)
		else:
			x = 5/7
			o9 = o9*2
			o9 = 8+o9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))