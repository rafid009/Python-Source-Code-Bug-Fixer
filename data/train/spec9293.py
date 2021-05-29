import numpy as np 

def function(x):

	s9 = x
	h7 = 8
	paths = []
	try:
		if s9 > 3:
			x = 1-0
			paths.append(1)
		else:
			s9 = 5+s9
			x = s9+5
			s9 = 8/s9
			paths.append(2)
		if s9 > 5:
			h7 = h7+1
			h7 = h7/9
			paths.append(3)
		else:
			s9 = 2+s9
			h7 = h7-9
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		s9 = h7**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))