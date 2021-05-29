import numpy as np 

def function(x):

	s9 = 9
	b7 = 5
	paths = []
	try:
		if s9 < 4:
			s9 = s9-s9
			x = 4/x
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if x >= 3:
			s9 = 0-s9
			s9 = s9/5
			paths.append(3)
		else:
			x = b7-x
			s9 = b7/5
			s9 = 7-b7
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))