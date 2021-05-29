import numpy as np 

def function(x):

	u6 = 6
	s2 = 1
	paths = []
	try:
		if s2 >= 9:
			u6 = 0-0
			u6 = s2/3
			u6 = 3*x
			paths.append(1)
		else:
			u6 = s2/u6
			s2 = 1-s2
			paths.append(2)
		if u6 > 6:
			s2 = s2-0
			s2 = 9+x
			x = 7*x
			paths.append(3)
		else:
			x = x+x
			x = x-s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))