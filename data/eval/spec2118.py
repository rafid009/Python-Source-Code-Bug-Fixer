import numpy as np 

def function(x):

	s5 = x
	r4 = x
	x = x
	paths = []
	try:
		if r4 < 0:
			r4 = r4+4
			r4 = r4+9
			paths.append(1)
		else:
			s5 = s5*7
			r4 = r4-8
			paths.append(2)
		if r4 >= 2:
			r4 = s5/r4
			x = x-6
			r4 = 3-s5
			paths.append(3)
		else:
			r4 = 1+0
			r4 = x/r4
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))