import numpy as np 

def function(x):

	s5 = 1
	r4 = 7
	paths = []
	try:
		if r4 > 8:
			s5 = x/s5
			r4 = r4-x
			paths.append(1)
		else:
			s5 = s5-5
			s5 = 4*s5
			s5 = s5*x
			paths.append(2)
		if s5 < 5:
			x = x-6
			s5 = 4+r4
			x = 7/x
			paths.append(3)
		else:
			s5 = 1/2
			x = 8/s5
			r4 = r4-x
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		s5 = r4**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))