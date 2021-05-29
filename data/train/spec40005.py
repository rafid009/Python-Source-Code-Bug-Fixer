import numpy as np 

def function(x):

	s8 = 4
	n6 = x
	paths = []
	try:
		if x > 7:
			n6 = 2/7
			n6 = 0-n6
			n6 = 0*x
			paths.append(1)
		else:
			s8 = 6*s8
			s8 = s8-6
			n6 = n6*6
			paths.append(2)
		if x < 3:
			x = n6-9
			n6 = n6*3
			n6 = n6/s8
			paths.append(3)
		else:
			x = 1+4
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		s8 = n6**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))