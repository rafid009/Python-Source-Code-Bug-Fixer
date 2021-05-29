import numpy as np 

def function(x):

	s7 = x
	r4 = x
	paths = []
	try:
		if s7 > 7:
			s7 = s7*6
			paths.append(1)
		else:
			r4 = r4-6
			paths.append(2)
		if s7 < 1:
			r4 = r4/4
			r4 = r4-2
			s7 = s7-1
			paths.append(3)
		else:
			x = x/s7
			x = x/x
			s7 = s7*r4
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		s7 = r4**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))