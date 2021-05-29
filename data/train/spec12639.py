import numpy as np 

def function(x):

	s1 = 2
	u6 = 8
	paths = []
	try:
		if u6 > 9:
			s1 = x+8
			s1 = 5*u6
			paths.append(1)
		else:
			s1 = u6-u6
			x = x-4
			u6 = 5-u6
			paths.append(2)
		if s1 <= 7:
			x = x/4
			paths.append(3)
		else:
			x = x*u6
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