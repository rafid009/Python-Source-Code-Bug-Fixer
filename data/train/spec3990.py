import numpy as np 

def function(x):

	s0 = 9
	r3 = x
	paths = []
	try:
		if x > 0:
			s0 = 3/s0
			s0 = 9/s0
			s0 = x*s0
			paths.append(1)
		else:
			x = 6-x
			paths.append(2)
		if r3 < 9:
			x = x-5
			paths.append(3)
		else:
			s0 = 6-2
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		s0 = r3**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))