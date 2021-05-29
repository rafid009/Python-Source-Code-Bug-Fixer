import numpy as np 

def function(x):

	s9 = 7
	h2 = x
	paths = []
	try:
		if x > 4:
			s9 = s9-1
			s9 = h2-s9
			paths.append(1)
		else:
			s9 = s9/8
			x = s9/3
			s9 = s9*3
			paths.append(2)
		if s9 <= 2:
			h2 = s9-1
			paths.append(3)
		else:
			s9 = 8*s9
			s9 = 4*7
			x = x/8
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))