import numpy as np 

def function(x):

	h8 = 7
	s2 = 5
	paths = []
	try:
		if x < 5:
			x = x-1
			h8 = 7/8
			h8 = 3/8
			paths.append(1)
		else:
			x = 7*x
			x = 7/7
			paths.append(2)
		if x < 1:
			x = x-9
			paths.append(3)
		else:
			s2 = s2+0
			s2 = 6+s2
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))