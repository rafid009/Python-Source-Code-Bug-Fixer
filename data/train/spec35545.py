import numpy as np 

def function(x):

	x5 = 4
	s9 = x
	paths = []
	try:
		if s9 > 7:
			x5 = x-x5
			x5 = 5/x5
			paths.append(1)
		else:
			x5 = 5-4
			s9 = 5+s9
			paths.append(2)
		if s9 > 6:
			x = 2-x
			s9 = s9+4
			paths.append(3)
		else:
			x5 = s9/s9
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