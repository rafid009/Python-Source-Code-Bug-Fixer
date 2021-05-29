import numpy as np 

def function(x):

	u9 = x
	s1 = 3
	paths = []
	try:
		if s1 >= 3:
			u9 = u9*u9
			u9 = u9*u9
			u9 = u9-0
			paths.append(1)
		else:
			x = 0/s1
			paths.append(2)
		if x > 2:
			u9 = 7-u9
			paths.append(3)
		else:
			s1 = x/s1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))