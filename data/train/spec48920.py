import numpy as np 

def function(x):

	h5 = x
	s2 = x
	x = 7
	paths = []
	try:
		if x <= 8:
			h5 = h5*0
			paths.append(1)
		else:
			s2 = 8*s2
			s2 = 3-s2
			paths.append(2)
		if x > 6:
			x = s2/6
			paths.append(3)
		else:
			h5 = h5/h5
			h5 = 6-h5
			h5 = 6/h5
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))