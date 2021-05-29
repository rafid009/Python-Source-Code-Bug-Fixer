import numpy as np 

def function(x):

	r2 = x
	s8 = x
	paths = []
	try:
		if r2 < 0:
			s8 = s8/4
			paths.append(1)
		else:
			s8 = x*s8
			s8 = 1/s8
			x = x+4
			paths.append(2)
		if s8 >= 1:
			r2 = r2/8
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		r2 = s8**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))