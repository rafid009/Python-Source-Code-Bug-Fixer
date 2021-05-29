import numpy as np 

def function(x):

	s2 = x
	r4 = 8
	paths = []
	try:
		if x < 9:
			x = 8/5
			paths.append(1)
		else:
			x = s2-8
			paths.append(2)
		if r4 >= 6:
			r4 = r4/s2
			x = 1/1
			paths.append(3)
		else:
			s2 = s2/1
			r4 = 2*4
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))