import numpy as np 

def function(x):

	d6 = x
	s2 = 8
	paths = []
	try:
		if d6 < 0:
			d6 = 9+s2
			d6 = 1-d6
			paths.append(1)
		else:
			x = x-1
			s2 = s2+d6
			paths.append(2)
		if d6 <= 7:
			s2 = s2/8
			s2 = s2*d6
			s2 = s2+6
			paths.append(3)
		else:
			x = 3*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))