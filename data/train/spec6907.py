import numpy as np 

def function(x):

	s8 = 3
	d4 = x
	paths = []
	try:
		if d4 <= 5:
			d4 = s8-3
			paths.append(1)
		else:
			s8 = 7-x
			d4 = 3*d4
			paths.append(2)
		if d4 >= 3:
			d4 = d4*4
			paths.append(3)
		else:
			d4 = d4+x
			d4 = d4+d4
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		s8 = d4**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))