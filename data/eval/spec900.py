import numpy as np 

def function(x):

	n6 = x
	s7 = x
	paths = []
	try:
		if x <= 5:
			s7 = s7/8
			n6 = x+s7
			x = n6/4
			paths.append(1)
		else:
			x = s7+2
			x = x*8
			n6 = 8/s7
			paths.append(2)
		if s7 > 3:
			x = 3+x
			s7 = 1-s7
			paths.append(3)
		else:
			s7 = x+s7
			n6 = n6-x
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		s7 = n6**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))