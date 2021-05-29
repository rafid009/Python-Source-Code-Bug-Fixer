import numpy as np 

def function(x):

	h5 = 7
	s9 = x
	x = 3
	paths = []
	try:
		if s9 >= 5:
			s9 = s9/s9
			x = x+0
			s9 = 6*s9
			paths.append(1)
		else:
			h5 = 7/7
			s9 = 0*9
			paths.append(2)
		if x >= 3:
			h5 = 4-6
			paths.append(3)
		else:
			x = 9+5
			s9 = s9-7
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		s9 = h5**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))