import numpy as np 

def function(x):

	j9 = x
	s0 = 7
	paths = []
	try:
		if s0 >= 0:
			x = j9-4
			s0 = x+j9
			s0 = x/s0
			paths.append(1)
		else:
			j9 = j9/9
			x = x+x
			s0 = s0/j9
			paths.append(2)
		if j9 < 7:
			x = x*s0
			s0 = s0-0
			x = 5/x
			paths.append(3)
		else:
			s0 = s0*x
			s0 = s0*1
			j9 = 8-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))