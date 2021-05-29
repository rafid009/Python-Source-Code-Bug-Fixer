import numpy as np 

def function(x):

	r3 = 1
	s0 = 6
	x = 7
	paths = []
	try:
		if s0 < 4:
			s0 = s0-1
			paths.append(1)
		else:
			r3 = r3/7
			s0 = s0-4
			s0 = s0/r3
			paths.append(2)
		if s0 > 6:
			r3 = r3-6
			paths.append(3)
		else:
			r3 = 8-8
			r3 = 5+x
			r3 = 8/1
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		r3 = r3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))