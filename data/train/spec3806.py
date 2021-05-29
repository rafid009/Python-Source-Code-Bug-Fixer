import numpy as np 

def function(x):

	s6 = x
	v4 = x
	paths = []
	try:
		if v4 <= 6:
			s6 = s6/s6
			v4 = 6-3
			x = x+4
			paths.append(1)
		else:
			s6 = 9+9
			v4 = v4-s6
			paths.append(2)
		if v4 <= 4:
			x = x/v4
			paths.append(3)
		else:
			x = x/9
			v4 = v4/v4
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