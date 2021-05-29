import numpy as np 

def function(x):

	s5 = 4
	a0 = 0
	paths = []
	try:
		if a0 < 7:
			x = 0-x
			paths.append(1)
		else:
			s5 = s5-7
			paths.append(2)
		if x >= 3:
			s5 = 2/s5
			a0 = a0-7
			paths.append(3)
		else:
			a0 = a0-x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		s5 = a0**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))