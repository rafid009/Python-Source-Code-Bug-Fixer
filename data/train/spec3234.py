import numpy as np 

def function(x):

	s6 = 8
	r4 = x
	paths = []
	try:
		if r4 > 1:
			r4 = x-r4
			paths.append(1)
		else:
			s6 = s6/5
			r4 = r4-1
			x = 0-x
			paths.append(2)
		if x < 5:
			s6 = 5/s6
			paths.append(3)
		else:
			s6 = s6-7
			r4 = 8/7
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		s6 = r4**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))