import numpy as np 

def function(x):

	v4 = x
	s2 = x
	paths = []
	try:
		if x >= 6:
			s2 = s2*6
			s2 = 2/s2
			x = x-5
			paths.append(1)
		else:
			x = 9*s2
			v4 = v4+3
			s2 = 9-s2
			paths.append(2)
		if v4 <= 8:
			x = x/x
			paths.append(3)
		else:
			v4 = 7+v4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))