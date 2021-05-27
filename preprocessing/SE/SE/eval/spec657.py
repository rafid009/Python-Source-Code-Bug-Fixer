import numpy as np 

def function(x):

	t8 = x
	s6 = 5
	paths = []
	try:
		if x >= 5:
			x = x+t8
			x = s6/s6
			paths.append(1)
		else:
			x = 2*x
			s6 = t8/s6
			x = x*s6
			paths.append(2)
		if x > 7:
			x = x+6
			x = 1-x
			paths.append(3)
		else:
			t8 = 5/3
			t8 = 0+3
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