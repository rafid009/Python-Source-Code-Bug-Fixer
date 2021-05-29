import numpy as np 

def function(x):

	u1 = x
	s6 = x
	paths = []
	try:
		if s6 >= 1:
			x = 4-x
			u1 = u1+u1
			x = 7*u1
			paths.append(1)
		else:
			s6 = 8-s6
			u1 = x+1
			u1 = 4/4
			paths.append(2)
		if s6 < 3:
			u1 = u1-5
			paths.append(3)
		else:
			u1 = u1-s6
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		s6 = u1**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))