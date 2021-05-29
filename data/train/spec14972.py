import numpy as np 

def function(x):

	s2 = x
	u1 = x
	x = 5
	paths = []
	try:
		if u1 < 2:
			u1 = 1-s2
			paths.append(1)
		else:
			s2 = s2+8
			x = u1-4
			u1 = 2*x
			paths.append(2)
		if s2 < 2:
			s2 = s2*6
			x = 2/9
			s2 = u1-2
			paths.append(3)
		else:
			x = x/9
			s2 = u1+u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))