import numpy as np 

def function(x):

	r9 = 9
	s0 = x
	x = x
	paths = []
	try:
		if s0 >= 2:
			s0 = s0-8
			s0 = s0*7
			x = 5-x
			paths.append(1)
		else:
			r9 = 3+s0
			s0 = s0*6
			s0 = s0/4
			paths.append(2)
		if r9 > 8:
			s0 = 3+5
			x = s0/9
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		s0 = r9**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))