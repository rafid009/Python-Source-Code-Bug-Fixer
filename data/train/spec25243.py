import numpy as np 

def function(x):

	r9 = 7
	s0 = x
	paths = []
	try:
		if r9 >= 5:
			x = r9/x
			r9 = r9/r9
			x = x+3
			paths.append(1)
		else:
			r9 = s0-r9
			r9 = 9*r9
			paths.append(2)
		if x <= 0:
			r9 = 0/x
			s0 = s0*0
			paths.append(3)
		else:
			r9 = r9-4
			r9 = r9/4
			r9 = 5-r9
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