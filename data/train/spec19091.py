import numpy as np 

def function(x):

	u0 = 6
	s0 = 6
	paths = []
	try:
		if u0 > 7:
			u0 = u0*1
			u0 = u0/x
			paths.append(1)
		else:
			u0 = 6/x
			u0 = 1*u0
			paths.append(2)
		if s0 >= 8:
			s0 = s0-s0
			u0 = 5/u0
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		u0 = u0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))