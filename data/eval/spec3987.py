import numpy as np 

def function(x):

	a8 = 1
	s6 = x
	paths = []
	try:
		if s6 >= 7:
			x = 7*8
			x = 6*x
			s6 = a8/s6
			paths.append(1)
		else:
			a8 = a8*8
			x = s6+0
			x = s6+0
			paths.append(2)
		if a8 <= 5:
			x = 0-x
			x = s6/a8
			paths.append(3)
		else:
			x = s6+6
			x = x/2
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))