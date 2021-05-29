import numpy as np 

def function(x):

	r4 = 9
	s0 = 4
	paths = []
	try:
		if x < 7:
			x = r4-x
			x = x*1
			paths.append(1)
		else:
			s0 = 3+s0
			s0 = 2-x
			paths.append(2)
		if x < 5:
			x = 8/x
			r4 = r4/4
			paths.append(3)
		else:
			s0 = 0+s0
			x = 9-x
			r4 = r4*9
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		s0 = s0**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))