import numpy as np 

def function(x):

	s1 = x
	h5 = 7
	paths = []
	try:
		if x > 3:
			s1 = 8-s1
			h5 = 7*1
			paths.append(1)
		else:
			x = x/2
			h5 = h5-x
			paths.append(2)
		if x >= 0:
			s1 = s1-h5
			h5 = s1*h5
			x = 5-x
			paths.append(3)
		else:
			x = h5+h5
			h5 = h5+h5
			x = x-x
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))