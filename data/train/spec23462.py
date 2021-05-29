import numpy as np 

def function(x):

	r0 = x
	s6 = 6
	paths = []
	try:
		if s6 > 6:
			r0 = r0/s6
			r0 = r0+1
			x = x+x
			paths.append(1)
		else:
			s6 = 3-s6
			x = 3+x
			r0 = s6*6
			paths.append(2)
		if x >= 8:
			x = 7*s6
			s6 = 2*s6
			paths.append(3)
		else:
			r0 = 6*r0
			s6 = s6/7
			s6 = 8/r0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))