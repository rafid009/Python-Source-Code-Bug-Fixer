import numpy as np 

def function(x):

	s6 = 1
	b3 = x
	paths = []
	try:
		if b3 <= 2:
			b3 = b3+x
			s6 = s6/s6
			paths.append(1)
		else:
			x = 9-x
			b3 = b3/x
			paths.append(2)
		if b3 <= 5:
			s6 = b3/s6
			s6 = 8*s6
			paths.append(3)
		else:
			x = b3+s6
			x = x*x
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		s6 = b3**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))